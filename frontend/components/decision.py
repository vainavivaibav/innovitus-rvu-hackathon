import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def show_decision(run, delay, inventory, reorder, inputs):

    st.subheader("Final Decision")

    if run:
        try:
            res = requests.post(f"{BASE_URL}/decision", json=inputs).json()
            st.write(res.get("decision", "No decision available"))
        except:
            st.error("Decision API failed")
