import streamlit as st
import pandas as pd

def show_optimization():
    st.subheader("Optimization Comparison")

    table = pd.DataFrame({
        "Mode":["Fast","Cost","Eco"],
        "Time":["Low","Medium","High"],
        "Cost":["High","Low","Medium"],
        "Emission":["High","Medium","Low"]
    })

    st.table(table)
