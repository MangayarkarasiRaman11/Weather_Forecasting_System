import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load preprocessed data
data_path = "dataset/preprocessed_weather_data.csv"
df = pd.read_csv(data_path)

# Define features and target variable
X = df[['temperature', 'humidity', 'wind_speed', 'pressure']]
y = df['temperature']  # Predicting temperature as an example

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
models = {
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "SVM": SVR(kernel='rbf'),
    "KNN": KNeighborsRegressor(n_neighbors=5)
}

trained_models = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"{name} Performance:")
    print(f"MAE: {mean_absolute_error(y_test, predictions)}")
    print(f"MSE: {mean_squared_error(y_test, predictions)}")
    print("------------------------------")

    trained_models[name] = model
    joblib.dump(model, f"models/{name}_model.pkl")

print("Model training complete. Models saved in the 'models' directory.")
