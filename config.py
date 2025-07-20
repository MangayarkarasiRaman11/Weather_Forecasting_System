import os

class Config:
    API_KEY = os.getenv("OPENWEATHERMAP_API_KEY", "your_openweathermap_api_key")
    MODEL_PATH = "models/RandomForest_model.pkl"
    SCALER_PATH = "models/scaler.pkl"
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
