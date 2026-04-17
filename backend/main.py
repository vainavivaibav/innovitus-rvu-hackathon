from fastapi import FastAPI
import pandas as pd

from backend.services.gmaps_service import get_route_data
from backend.services.weather_service import get_weather_risk

from backend.data.loader import load_data
from backend.data.preprocess import preprocess

from backend.models.train import train_models
from backend.models.predict import predict_demand, predict_delay

from backend.services.inventory import reorder_point, inventory_status
from backend.services.optimization import select_best_supplier
from backend.services.routing import route_info
from backend.services.sustainability import calculate_emission
from backend.services.traffic import detect_spike
from backend.services.decision import make_decision

def get_filtered_sample(data):
    region_map = {
        "South": "South Asia",
        "North": "US"
    }

    sample = df.sample(10)

    if data and "region" in data:
        mapped_region = region_map.get(data["region"])

        if mapped_region:
            filtered = df[df["Order Region"] == mapped_region]

            if len(filtered) > 0:
                sample = filtered.sample(min(10, len(filtered)))

    return sample

app = FastAPI(title="AI Supply Chain API")

# Load + preprocess
df, log_df = load_data()
df = preprocess(df)

# Train models
demand_model, delay_model, d_cols, l_cols = train_models(df)

# ---------------- ROUTES ----------------

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict-demand")
def demand(data: dict):
    sample = get_filtered_sample(data)
    return {"predicted_demand": predict_demand(demand_model, d_cols, sample)}

@app.post("/predict-delay")
def delay(data: dict):
    sample = get_filtered_sample(data)
    return {"predicted_delay": predict_delay(delay_model, l_cols, sample)}

@app.post("/inventory-status")
def inventory(data: dict):
    sample = get_filtered_sample(data)

    demand = predict_demand(demand_model, d_cols, sample)
    reorder = reorder_point(demand, 3, 50)
    status = inventory_status(200, reorder)

    return {"stock": 200, "reorder": reorder, "status": status}

@app.post("/optimize")
def optimize(data: dict):
    sample = get_filtered_sample(data)

    best = select_best_supplier(sample)

    route = route_info(best)
    emission = calculate_emission(best['distance_km'], best['CO2_per_km'])

    gmaps = get_route_data()
    weather = get_weather_risk()

    return {
        "supplier": best['supplier_location'],
        "route": route,
        "emission": emission,
        "gmaps": gmaps,
        "weather": weather
    }

@app.post("/decision")
def decision(data: dict):
    sample = get_filtered_sample(data)

    demand = predict_demand(demand_model, d_cols, sample)[0]
    delay = predict_delay(delay_model, l_cols, sample)[0]

    reorder = reorder_point([demand], 3, 50)
    status = inventory_status(200, reorder)

    return {"decision": make_decision(demand, delay, status)}

@app.get("/traffic-insights")
def traffic():
    return {"insight": detect_spike(log_df)}