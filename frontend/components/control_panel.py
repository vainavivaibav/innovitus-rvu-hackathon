import streamlit as st

def control_panel():
    st.subheader("Control Panel")

    date = st.date_input("Select Date Range")
    product = st.selectbox("Product", ["A","B","C"])
    region = st.selectbox("Region", ["South","North"])
    shipping = st.selectbox("Shipping Mode", ["Standard","Express"])
    mode = st.radio("Priority Mode", ["Fast Delivery","Cost Efficient","Eco Friendly"])
    lead = st.number_input("Lead Time", value=3)
    stock = st.number_input("Safety Stock", value=50)

    run = st.button("Run Prediction")
    optimize = st.button("Optimize")

    return {
        "date": date,
        "product": product,
        "region": region,
        "shipping": shipping,
        "mode": mode,
        "lead": lead,
        "stock": stock,
        "run": run
    }
