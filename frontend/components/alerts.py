import streamlit as st
import numpy as np

def show_alerts(run, delay, inventory, reorder, demand):
    st.subheader("Alerts")

    if run:
        if delay > 70:
            st.error("Delivery delay risk")
        if inventory < reorder:
            st.warning("Inventory shortage")
        if np.mean(demand) > 160:
            st.info("Demand spike detected")
