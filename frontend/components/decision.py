import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def show_decision(run, delay, inventory, reorder):

    st.subheader("Final Decision")

    if run:
        res = requests.get(f"{BASE_URL}/decision").json()
        st.write(res["decision"])
