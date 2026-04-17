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
def demand():
    sample = df[df["Order Region"] == "South Asia"].head(20)
    return {"predicted_demand": predict_demand(demand_model, d_cols, sample)}

@app.post("/predict-delay")
def delay():
    sample = df[df["Order Region"] == "South Asia"].head(20)
    return {"predicted_delay": predict_delay(delay_model, l_cols, sample)}

@app.get("/inventory-status")
def inventory():
    sample = df[df["Order Region"] == "South Asia"].head(20)
    demand = predict_demand(demand_model, d_cols, sample)

    reorder = reorder_point(demand, 3, 50)
    status = inventory_status(200, reorder)

    return {"stock": 200, "reorder": reorder, "status": status}

@app.get("/optimize")
def optimize():
    best = select_best_supplier(df)

    # Existing logic
    route = route_info(best)
    emission = calculate_emission(best['distance_km'], best['CO2_per_km'])

    # NEW APIs
    gmaps = get_route_data()
    weather = get_weather_risk()

    return {
        "supplier": best['supplier_location'],
        "route": route,
        "emission": emission,

        # NEW DATA
        "gmaps": gmaps,
        "weather": weather
    }

@app.get("/decision")
def decision():
    sample = df[df["Order Region"] == "South Asia"].head(20)

    demand = predict_demand(demand_model, d_cols, sample)[0]
    delay = predict_delay(delay_model, l_cols, sample)[0]

    reorder = reorder_point([demand], 3, 50)
    status = inventory_status(200, reorder)

    return {"decision": make_decision(demand, delay, status)}

@app.get("/traffic-insights")
def traffic():
    return {"insight": detect_spike(log_df)}