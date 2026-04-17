import requests
import streamlit as st
import pandas as pd
import numpy as np

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")
st.title("🚀 AI Supply Chain Dashboard")

# ---------------- CONTROL PANEL ----------------
run = st.sidebar.button("Run Prediction")

# ---------------- MAIN ----------------
if run:

    demand = requests.post(f"{BASE_URL}/predict-demand").json()["predicted_demand"]
    delay = requests.post(f"{BASE_URL}/predict-delay").json()["predicted_delay"]
    inventory_res = requests.get(f"{BASE_URL}/inventory-status").json()
    optimize_res = requests.get(f"{BASE_URL}/optimize").json()
    decision_res = requests.get(f"{BASE_URL}/decision").json()
    traffic_res = requests.get(f"{BASE_URL}/traffic-insights").json()

    # ---------------- METRICS ----------------
    st.subheader("📊 Key Metrics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Orders", "1200")
    c2.metric("Predicted Demand", int(np.mean(demand)))
    c3.metric("Delay Risk", f"{delay}%")
    c4.metric("Revenue", "₹2.5L")

    # ---------------- DEMAND CHART ----------------
    st.subheader("📈 Demand Forecast")

    df = pd.DataFrame({
        "Day": range(1, len(demand)+1),
        "Demand": demand
    })

    st.line_chart(df.set_index("Day"))

    if np.mean(demand) > 150:
        st.warning("High demand expected")
    else:
        st.success("Demand stable")

    # ---------------- DELAY ----------------
    st.subheader("⏱ Delay Risk")

    if delay > 70:
        st.error(f"High Risk ({delay}%)")
    elif delay > 50:
        st.warning(f"Medium Risk ({delay}%)")
    else:
        st.success(f"Low Risk ({delay}%)")

    # ---------------- INVENTORY ----------------
    st.subheader("📦 Inventory Status")

    col1, col2 = st.columns(2)

    col1.metric("Stock", inventory_res["stock"])
    col2.metric("Reorder Point", int(inventory_res["reorder"]))

    if inventory_res["status"] == "SAFE":
        st.success("Inventory is Safe")
    elif inventory_res["status"] == "LOW":
        st.warning("Inventory is Low")
    else:
        st.error("Inventory Critical")

    # ---------------- OPTIMIZATION ----------------
    st.subheader("🚚 Optimization Recommendation")

    st.write(f"**Supplier:** {optimize_res['supplier']}")
    st.write(f"**Distance:** {optimize_res['route']['distance']} km")
    st.write(f"**Time:** {round(optimize_res['route']['time'],2)} days")
    st.write(f"**CO₂ Emission:** {round(optimize_res['emission'],2)} kg")

    if delay > 70:
        st.error("⚠ Switch supplier or route")

    # ---------------- TRAFFIC ----------------
    st.subheader("🚦 Traffic Insights")

    st.info(traffic_res["insight"])

    traffic = np.random.randint(50, 200, 10)
    st.line_chart(traffic)

    # ---------------- DECISION ----------------
    st.subheader("🧠 Final AI Decision")

    st.success(decision_res["decision"])