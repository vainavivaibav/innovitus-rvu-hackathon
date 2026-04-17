import requests

BASE_URL = "http://127.0.0.1:8000"

def simulate(inputs):

    # Demand
    demand_res = requests.post(f"{BASE_URL}/predict-demand").json()
    demand = demand_res["predicted_demand"]

    # Delay
    delay_res = requests.post(f"{BASE_URL}/predict-delay").json()
    delay_raw = delay_res["predicted_delay"][0]
    delay_prob = int(delay_raw * 100)

    # Inventory
    inv_res = requests.get(f"{BASE_URL}/inventory-status").json()
    inventory = inv_res["stock"]
    reorder = int(inv_res["reorder"])

    return demand, delay_prob, inventory, reorder