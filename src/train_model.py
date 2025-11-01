# src/train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

# ✅ Load dataset
data_path = os.path.join("data", "Food_Delivery_Times.csv")
df = pd.read_csv(data_path)

print(f"✅ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ✅ Handle missing values
df = df.dropna()

# ✅ Drop irrelevant columns
if 'Order_ID' in df.columns:
    df = df.drop(columns=['Order_ID'])

# ✅ Encode categorical columns
label_encoders = {}
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# ✅ Define features and target
X = df.drop("Delivery_Time_min", axis=1)
y = df["Delivery_Time_min"]

# ✅ Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# ✅ Evaluate model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n📊 Model Evaluation:")
print(f"R² Score: {r2:.3f}")
print(f"MAE: {mae:.2f} minutes")
print(f"RMSE: {rmse:.2f} minutes")

# ✅ Save model and encoders
os.makedirs("model", exist_ok=True)
model_path = os.path.join("model", "food_delivery_model.pkl")
encoders_path = os.path.join("model", "encoders.pkl")

joblib.dump(model, model_path)
joblib.dump(label_encoders, encoders_path)

print(f"\n💾 Model saved at: {model_path}")
print(f"💾 Encoders saved at: {encoders_path}")