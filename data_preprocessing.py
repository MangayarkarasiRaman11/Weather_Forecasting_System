import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib


def load_data(file_path):
    """Load dataset from a CSV file."""
    return pd.read_csv(file_path)


def preprocess_data(df):
    """Clean and preprocess the dataset."""

    # Handling missing values
    imputer = SimpleImputer(strategy='mean')
    df[['temperature', 'humidity', 'wind_speed', 'pressure']] = imputer.fit_transform(
        df[['temperature', 'humidity', 'wind_speed', 'pressure']]
    )

    # Standardizing the numerical features
    scaler = StandardScaler()
    df[['temperature', 'humidity', 'wind_speed', 'pressure']] = scaler.fit_transform(
        df[['temperature', 'humidity', 'wind_speed', 'pressure']]
    )

    return df, scaler


def save_preprocessed_data(df, output_path):
    """Save the cleaned dataset."""
    df.to_csv(output_path, index=False)


def save_scaler(scaler, scaler_path):
    """Save the trained scaler for later use."""
    joblib.dump(scaler, scaler_path)


if __name__ == "__main__":
    # Load dataset
    data_path = "dataset/weather_data.csv"  # Update with actual dataset path
    df = load_data(data_path)

    # Preprocess dataset
    df, scaler = preprocess_data(df)

    # Save preprocessed data and scaler
    save_preprocessed_data(df, "dataset/preprocessed_weather_data.csv")
    save_scaler(scaler, "models/scaler.pkl")

    print("Data preprocessing complete. Preprocessed data and scaler saved.")
