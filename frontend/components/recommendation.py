import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def show_recommendation(run, delay):

    st.subheader("AI Recommendation")

    if run:
        res = requests.get(f"{BASE_URL}/optimize").json()

        st.write(f"Supplier: {res['supplier']}")
        st.write(f"Route Distance: {res['route']['distance']} km")
        st.write(f"Time: {round(res['route']['time'], 2)} hrs")
        st.write(f"CO₂: {round(res['emission'], 2)} kg")

        if delay > 70:
            st.error("Switch supplier or route")