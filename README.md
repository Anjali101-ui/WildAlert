<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# WildAlert 🎯

## Basic Details

### Team Name: Pixel Petals

### Team Members
- Member 1: Anjali Kizhakekuttu Thomas - Saintgits College of Engineering
- Member 2: Anjana Benny -  Saintgits College of Engineering

### Hosted Project Link
[mention your project hosted link here]

### Project Description
WildGuard is a real-time wildlife monitoring system that uses AI to detect animals from live video feeds. It analyzes their movement, calculates risk levels, and provides instant alerts to forest officers to help prevent human-animal conflicts.

### The Problem statement
Forest officers cannot continuously monitor wildlife movement across large forest areas. This lack of real-time monitoring often leads to delayed responses, accidents, and increased human-animal conflicts.

### The Solution
WildGuard uses YOLOv8-based AI detection, movement tracking, and risk assessment logic to provide real-time alerts and dashboard insights. This enables faster decision-making and proactive response to potential wildlife threats.
---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Python 3
- Frameworks used: Streamlit
- Libraries used: 
    - OpenCV (for video processing)
    - YOLOv8 – Ultralytics (for animal detection)
    - Pandas (for data handling)
    - SQLite (for event logging)
    - Folium / Leaflet.js (for map visualization)
- Tools used: VS Code, Git

**For Hardware:**
- Main components:
    - Webcam or IP Camera
    - Laptop/PC
- Specifications: 
    - Python 3.9 or above
    - Minimum 8GB RAM recommended for smooth YOLO processing
    - Internet connection (required for loading map tiles)
- Tools required: 
    - Stable power supply
    - Internet connection

---

## Features

List the key features of your project:
- Real-time Animal Detection: Detects multiple animals in live video streams using AI (YOLOv8) with bounding boxes and classification.
- Risk Assessment: Calculates animal speed, direction, ETA, and proximity to human areas to determine Low, Medium, or High risk.
- Interactive Dashboard: Streamlit-based dashboard displays live video, alert panels, and detection details for forest officers.
- Map Integration: Uses Leaflet.js and OpenStreetMap to visualize animal locations on an interactive map.
- Alerts & Notifications: Provides real-time alerts for high-risk animal movement to help prevent human-animal conflicts.
- Optional Database Logging: Stores detection events, timestamps, and risk data for future analysis or reporting.

---

## Implementation

### For Software:

#### Installation
```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate virtual environment
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install required Python libraries
python3 -m pip install -r requirements.txt

#### Run
# Run the Streamlit dashboard
python3 dashboard.py

# Or, if using Streamlit command
streamlit run dashboard.py

### For Hardware:

#### Components Required
  - Webcam or IP Camera
  - Minimum 720p resolution recommended
  - Used for capturing live wildlife video feed
  - Laptop / PC
  - Minimum 8GB RAM (recommended for YOLOv8 processing)
  - Python 3.9+ installed
  - Internet connection for map visualization
  - Internet Connection
  - Required for OpenStreetMap tiles and dashboard loading

#### Circuit Setup
No physical circuit was required for this implementation.
The webcam (or IP camera) is directly connected to the system via USB or network connection. The live feed is processed using YOLOv8 for animal detection, and results are displayed on the Streamlit dashboard.
The system architecture is software-driven rather than hardware-circuit based.

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![img2](https://github.com/user-attachments/assets/b5d820d3-2147-4973-89f0-32ac01adf05f)

#### Diagrams

**System Architecture:**

![img1](https://github.com/user-attachments/assets/551e6f39-4f7e-4429-b7ea-d7ac11bccfac)

**Application Workflow:**
Capture Video – The camera records live video from the forest.
Detect Animals – YOLOv8 AI model identifies animals in each video frame.
Check Risk – The system calculates how fast animals are moving, where they are going, and if they are near humans to determine Low, Medium, or High risk.
Show on Dashboard – Live video, detected animals, and their risk levels appear on the Streamlit dashboard.
Map Animals – Animal locations are shown on a map using Leaflet and OpenStreetMap.
Send Alerts – High-risk animals trigger alerts so forest officers can act quickly.
---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
https://drive.google.com/drive/folders/1wDOPNN6Q7rzIl1KMxqvwnTWw-lATbhe4

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used: ChatGPT

**Purpose:** 
- Assisted in writing Python code snippets for Streamlit dashboard and YOLOv8 integration.
- Helped structure README documentation, workflow diagrams, and project descriptions.
- Provided suggestions for risk calculation logic and dashboard layout.


**Key Prompts Used:**
- Create a Streamlit dashboard for real-time video with bounding boxes.
- Generate Python code to calculate animal speed and risk level from video frames.
- Write a README template for a hackathon project.
- Explain application workflow in simple words.

**Percentage of AI-generated code:** Approximately 20–30%

**Human Contributions:**
- Architecture design and planning of the system workflow.
- Custom business logic implementation for risk analysis.
- Integration and testing of YOLOv8, Streamlit, and Map features.
- UI/UX design decisions for the dashboard and alert panels.
- Final code review, debugging, and deployment.

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

-Anjali Kizhakekuttu Thomas : [Specific contributions - e.g., Frontend development, API integration, etc.]
- Anjana Benny: [Specific contributions - e.g., Backend development, Database design, etc.]
---

## License

This project is licensed under the *MIT License* - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
