from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import pandas as pd
import joblib
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# ✅ Load model and encoders
model = joblib.load("model/food_delivery_model.pkl")
label_encoders = joblib.load("model/encoders.pkl")

# ✅ Dropdown options (match training data categories)
weather_options = ["Clear", "Rainy", "Foggy", "Windy"]
traffic_options = ["Low", "Medium", "High"]
timeofday_options = ["Morning", "Afternoon", "Evening", "Night"]
vehicle_options = ["Bike", "Scooter"]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": None,
            "weather_options": weather_options,
            "traffic_options": traffic_options,
            "timeofday_options": timeofday_options,
            "vehicle_options": vehicle_options,
            "error": None,
        },
    )

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    distance: float = Form(...),
    weather: str = Form(...),
    traffic: str = Form(...),
    time_of_day: str = Form(...),
    vehicle: str = Form(...),
    prep_time: int = Form(...),
    courier_exp: float = Form(...),
):
    try:
        # ✅ Create DataFrame
        input_data = pd.DataFrame(
            [[distance, weather, traffic, time_of_day, vehicle, prep_time, courier_exp]],
            columns=[
                "Distance_km",
                "Weather",
                "Traffic_Level",
                "Time_of_Day",
                "Vehicle_Type",
                "Preparation_Time_min",
                "Courier_Experience_yrs",
            ],
        )

        # ✅ Encode categorical columns
        for col in label_encoders.keys():
            if col in input_data.columns:
                le = label_encoders[col]
                if input_data[col][0] in le.classes_:
                    input_data[col] = le.transform(input_data[col])
                else:
                    raise ValueError(f"Unknown category '{input_data[col][0]}' for '{col}'")

        # ✅ Predict
        pred = model.predict(input_data)[0]

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction": round(pred, 2),
                "weather_options": weather_options,
                "traffic_options": traffic_options,
                "timeofday_options": timeofday_options,
                "vehicle_options": vehicle_options,
                "error": None,
            },
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction": None,
                "weather_options": weather_options,
                "traffic_options": traffic_options,
                "timeofday_options": timeofday_options,
                "vehicle_options": vehicle_options,
                "error": f"⚠️ Error: {str(e)}",
            },
        )