from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

# Load datasets
df = pd.read_csv("datasets/dataset1.csv")
log_df = pd.read_csv("datasets/dataset2.csv")

# -------------------- HELPERS --------------------

def preprocess(df):
    df = df.dropna()

    df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'])
    df['shipping date (DateOrders)'] = pd.to_datetime(df['shipping date (DateOrders)'])

    df['order_day'] = df['order date (DateOrders)'].dt.day
    df['order_month'] = df['order date (DateOrders)'].dt.month
    df['order_hour'] = df['order date (DateOrders)'].dt.hour

    df['delay'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']
    return df

df = preprocess(df)

# -------------------- ROUTES --------------------

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/predict-demand")
def predict_demand():
    demand = np.random.randint(100, 200, 7).tolist()
    return {"predicted_demand": demand}

@app.post("/predict-delay")
def predict_delay():
    delay = int(np.random.randint(40, 90))
    return {"predicted_delay": delay}

@app.get("/inventory-status")
def inventory():
    demand = np.random.randint(100, 200, 7)
    reorder = int(np.mean(demand) * 3 + 50)
    stock = 200

    if stock > reorder:
        status = "SAFE"
    elif stock > reorder * 0.7:
        status = "LOW"
    else:
        status = "CRITICAL"

    return {
        "stock": stock,
        "reorder": reorder,
        "status": status
    }

@app.get("/optimize")
def optimize():
    return {
        "supplier": "Chennai Hub",
        "route": {
            "distance": 120,
            "time": 2.5
        },
        "emission": 95
    }

@app.get("/decision")
def decision():
    delay = int(np.random.randint(40, 90))
    inventory = 200
    reorder = 180

    if delay > 70:
        decision = "Switch supplier or route"
    elif inventory < reorder:
        decision = "Reorder stock"
    else:
        decision = "Operations normal"

    return {"decision": decision}

@app.get("/traffic-insights")
def traffic():
    hits = log_df.shape[0]

    if hits > 100:
        return {"insight": "High traffic → demand spike expected"}
    return {"insight": "Traffic normal"}