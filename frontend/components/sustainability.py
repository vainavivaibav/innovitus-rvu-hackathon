import streamlit as st

def show_sustainability(run):
    st.subheader("Sustainability")

    if run:
        st.progress(70)
        st.write("CO₂: 120 kg")
