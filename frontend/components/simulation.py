import requests

import random

BASE_URL = "http://127.0.0.1:8000"

def simulate(inputs):

    # Demand
    payload = {
    "region": inputs["region"],
    "product": inputs["product"],
    "shipping": inputs["shipping"],
    "lead": inputs["lead"]
}

    demand_res = requests.post(f"{BASE_URL}/predict-demand", json=payload).json()
    demand = demand_res["predicted_demand"]

    demand = [round(x * 10, 2) for x in demand]

    delay_res = requests.post(f"{BASE_URL}/predict-delay", json=payload).json()
    delay_raw = delay_res["predicted_delay"][0]
    delay_prob = int(delay_raw * 100)

    inv_res = requests.post(f"{BASE_URL}/inventory-status", json=payload).json()
    inventory = inv_res["stock"]
    reorder = int(inv_res["reorder"])

    return demand, delay_prob, inventory, reorder