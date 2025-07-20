import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 1000 rows of weather data
num_samples = 1000
start_date = datetime(2023, 1, 1)

weather_conditions = ["Sunny", "Cloudy", "Rainy", "Clear", "Partly Cloudy", "Overcast", "Stormy", "Snowy"]
data = {
    "Date": [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_samples)],
    "temperature": [round(random.uniform(-5, 40), 1) for _ in range(num_samples)],
    "humidity": [random.randint(30, 100) for _ in range(num_samples)],
    "wind_speed": [round(random.uniform(0, 20), 1) for _ in range(num_samples)],
    "pressure": [random.randint(980, 1050) for _ in range(num_samples)],
    "Weather Condition": [random.choice(weather_conditions) for _ in range(num_samples)]
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("weather_data.csv", index=False)

print("weather_data.csv created successfully!")

