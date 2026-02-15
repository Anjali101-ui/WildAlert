import { useEffect, useState } from "react";

function Tracking() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://127.0.0.1:5000/latest");
        const json = await res.json();
        setData(json);
      } catch (error) {
        console.error("Error fetching latest detection:", error);
      }
    };

    fetchData(); // initial call

    const interval = setInterval(fetchData, 3000); // update every 3 seconds

    return () => clearInterval(interval);
  }, []);

  const getRiskColor = (risk) => {
    switch (risk) {
      case "LOW":
        return "bg-green-500";
      case "MODERATE":
        return "bg-yellow-500";
      case "HIGH":
        return "bg-orange-500";
      case "CRITICAL":
        return "bg-red-600 animate-pulse";
      default:
        return "bg-gray-500";
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center p-6">

      {data && data.risk_level ? (
        <div
          className={`w-full max-w-xl p-8 rounded-2xl shadow-lg text-white transition-all duration-500 ${getRiskColor(
            data.risk_level
          )}`}
        >
          <h2 className="text-3xl font-bold mb-4 text-center">
            🚨 Wildlife Alert
          </h2>

          <div className="space-y-2 text-lg">
            <p><strong>Animal:</strong> {data.animal?.toUpperCase()}</p>
            <p><strong>Nearest Village:</strong> {data.nearest_village}</p>
            <p><strong>Distance:</strong> {data.distance_meters} meters</p>
            <p><strong>Speed:</strong> {data.speed_level}</p>
            <p><strong>Direction:</strong> {data.direction}</p>
            <p><strong>Risk Level:</strong> {data.risk_level}</p>
          </div>

          {data.ai_analysis && (
            <div className="mt-6 p-4 bg-black bg-opacity-20 rounded-lg">
              <h3 className="font-semibold mb-2">🤖 AI Analysis:</h3>
              <p className="text-sm whitespace-pre-line">
                {data.ai_analysis}
              </p>
            </div>
          )}
        </div>
      ) : (
        <div className="text-gray-600 text-xl">
          Waiting for wildlife detection...
        </div>
      )}
    </div>
  );
}

export default Tracking;
