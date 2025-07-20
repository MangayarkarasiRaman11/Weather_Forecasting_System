import requests
import numpy as np
import joblib
import pandas as pd

def fetch_real_time_weather(city, country, api_key):
    """Fetch real-time weather data from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching weather data")
        return None

    data = response.json()
    return {
        "temperature": data["main"].get("temp"),
        "humidity": data["main"].get("humidity"),
        "wind_speed": data["wind"].get("speed"),
        "pressure": data["main"].get("pressure"),
    }


def load_model(model_path):
    """Load trained machine learning model."""
    return joblib.load(model_path)


def predict_weather(model, weather_data, scaler):
    """Predict weather condition based on real-time data."""

    # Convert real-time data into a DataFrame with correct feature names
    features_df = pd.DataFrame([weather_data], columns=["temperature", "humidity", "wind_speed", "pressure"])

    # Scale input features
    scaled_features = scaler.transform(features_df)

    # Make a prediction
    prediction = model.predict(scaled_features)[0]

    return prediction


if __name__ == "__main__":
    city = "London"
    country = "UK"
    API_KEY = "ec59600738fd18afa52f8faa7f94154a"  # Replace with actual API key
    MODEL_PATH = "models/RandomForest_model.pkl"
    SCALER_PATH = "models/scaler.pkl"

    # Load model and scaler
    model = load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    # Fetch real-time weather data
    weather_data = fetch_real_time_weather(city, country, API_KEY)

    if weather_data:
        prediction = predict_weather(model, weather_data, scaler)
        print(f"Predicted Temperature: {prediction}°C")
