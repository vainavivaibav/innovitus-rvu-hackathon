import streamlit as st

def show_metrics(run, demand, delay):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Orders", "1200")
    c2.metric("Predicted Demand", sum(demand) if run else "--")
    c3.metric("Delay Risk", f"{delay}%" if run else "--")
    c4.metric("Revenue", "₹2.5L")
