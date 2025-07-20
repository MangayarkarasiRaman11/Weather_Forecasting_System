from flask import Flask, request, jsonify, render_template
import requests
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

API_KEY = "ec59600738fd18afa52f8faa7f94154a"  # Replace with your actual API key
MODEL_PATH = "models/RandomForest_model.pkl"  # Path to trained ML model

# Load trained machine learning model
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    country = request.args.get("country", "")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    data = response.json()
    weather_features = np.array([
        data["main"].get("temp"),
        data["main"].get("humidity"),
        data["wind"].get("speed"),
        data["main"].get("pressure"),
    ]).reshape(1, -1)

    prediction = model.predict(weather_features)[0]

    weather_info = {
        "city": data.get("name"),
        "country": data["sys"].get("country"),
        "temperature": data["main"].get("temp"),
        "feels_like": data["main"].get("feels_like"),
        "humidity": data["main"].get("humidity"),
        "longitude": data["coord"].get("lon"),
        "latitude": data["coord"].get("lat"),
        "description": data["weather"][0].get("description"),
        "prediction": prediction,
    }
    return jsonify(weather_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
