import streamlit as st
import pandas as pd

def show_map(run, delay):
    if run and delay > 70:
        st.subheader("Route Map")
        st.map(pd.DataFrame({
            "lat":[13.08,12.97],
            "lon":[80.27,77.59]
        }))
