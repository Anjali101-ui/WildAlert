from flask import Flask, Response
from ultralytics import YOLO
import cv2
import os
import time
import math
import requests
from datetime import datetime

app = Flask(__name__)

# -------------------- MODEL --------------------
model = YOLO("best.pt")

VIDEO_PATH = os.path.join(os.path.dirname(__file__), "../frontend/src/assets/assets/cctv.mp4")
print(f"Attempting to open video at: {VIDEO_PATH}")

CLASSES = ["tiger", "bear", "elephant", "wild boar", "lion", "wild buffalo"]

# -------------------- CAMERA GPS (Wayanad Forest Edge) --------------------
CAMERA_ID = "CAM_WAYANAD_01"
CAMERA_LAT = 11.6400
CAMERA_LON = 76.1200

# -------------------- NEARBY TOWNS IN WAYANAD --------------------
VILLAGES = [
    {"name": "Kalpetta", "lat": 11.6100, "lon": 76.0820},
    {"name": "Mananthavady", "lat": 11.8014, "lon": 76.0025},
    {"name": "Sulthan Bathery", "lat": 11.6656, "lon": 76.2731}
]

# -------------------- WEBHOOK --------------------
WEBHOOK_URL = "http://127.0.0.1:5678/webhook/wildlife-alert"


# -------------------- FUNCTIONS --------------------

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))


def get_direction(angle):
    if -22.5 <= angle < 22.5:
        return "E"
    elif 22.5 <= angle < 67.5:
        return "NE"
    elif 67.5 <= angle < 112.5:
        return "N"
    elif 112.5 <= angle < 157.5:
        return "NW"
    elif angle >= 157.5 or angle < -157.5:
        return "W"
    elif -157.5 <= angle < -112.5:
        return "SW"
    elif -112.5 <= angle < -67.5:
        return "S"
    else:
        return "SE"

# -------------------- MAIN LOOP --------------------

def generate_frames():
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {VIDEO_PATH}")
        return

    print("Video file opened successfully!")

    position_history = []
    prev_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        current_time = time.time()
        time_diff = current_time - prev_time
        prev_time = current_time

        results = model(frame)

        for result in results:
            boxes = result.boxes.xyxy
            confidences = result.boxes.conf
            class_ids = result.boxes.cls

            for i in range(len(boxes)):
                x1, y1, x2, y2 = map(int, boxes[i])
                class_id = int(class_ids[i])
                animal_name = CLASSES[class_id]
                confidence = confidences[i]

                # -------- CENTER --------
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                position_history.append((cx, cy))
                if len(position_history) > 5:
                    position_history.pop(0)

                if len(position_history) >= 2:
                    dx = position_history[-1][0] - position_history[0][0]
                    dy = position_history[-1][1] - position_history[0][1]
                else:
                    dx, dy = 0, 0

                speed = ((dx**2 + dy**2) ** 0.5) / time_diff if time_diff > 0 else 0

                if speed < 20:
                    speed_level = "Slow"
                elif speed < 50:
                    speed_level = "Moderate"
                else:
                    speed_level = "Fast"

                angle = math.degrees(math.atan2(dy, dx))
                direction = get_direction(angle)

                # -------- GEO DISTANCE --------
                nearest_distance = float('inf')
                nearest_village = None

                for v in VILLAGES:
                    d = haversine(CAMERA_LAT, CAMERA_LON, v["lat"], v["lon"])
                    if d < nearest_distance:
                        nearest_distance = d
                        nearest_village = v["name"]

                if nearest_distance < 300:
                    risk_level = "CRITICAL"
                elif nearest_distance < 700:
                    risk_level = "HIGH"
                elif nearest_distance < 1500:
                    risk_level = "MODERATE"
                else:
                    risk_level = "LOW"

                # -------- DATA --------
                data = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "animal": animal_name,
                    "camera_id": CAMERA_ID,
                    "lat": CAMERA_LAT,
                    "lon": CAMERA_LON,
                    "nearest_village": nearest_village,
                    "distance_meters": round(nearest_distance, 2),
                    "risk_level": risk_level,
                    "speed_level": speed_level,
                    "direction": direction
                }

                print(data)

                try:
                    response = requests.post(WEBHOOK_URL, json=data)
                    print("Webhook response:", response.status_code)
                except Exception as e:
                    print("Webhook error:", e)


                # -------- DRAWING --------
                label = f"{animal_name} ({risk_level})"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "WildAlert Backend is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
