import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def show_traffic(run):

    st.subheader("Traffic Insights")

    if run:
        res = requests.get(f"{BASE_URL}/traffic-insights").json()
        st.info(res["insight"])