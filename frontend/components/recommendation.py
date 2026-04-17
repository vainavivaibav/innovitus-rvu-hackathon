import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def show_recommendation(run, delay, inputs):

    st.subheader("AI Recommendation")

    if run:
        try:
            res = requests.post(f"{BASE_URL}/optimize", json=inputs, timeout=5).json()
        except Exception:
            st.error("⚠️ API Error")
            return

        route = res.get("route", {})

        st.write(f"Supplier: {res.get('supplier', 'N/A')}")
        st.write(f"Route Distance: {route.get('distance', 'N/A')} km")
        st.write(f"Time: {round(route.get('time', 0), 2)} hrs")
        st.write(f"CO₂: {round(res.get('emission', 0), 2)} kg")

        if delay > 70:
            st.error("Switch supplier or route")