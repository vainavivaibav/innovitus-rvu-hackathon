import streamlit as st
import pandas as pd
import numpy as np

def show_forecast(run, demand):
    st.subheader("Demand Forecast")

    if run:
        df = pd.DataFrame({
    "Day": range(1, len(demand) + 1),
    "Demand": demand
})
        st.line_chart(df.set_index("Day"))

        if np.mean(demand) > 150:
            st.info("Demand expected to increase in next cycle")
        else:
            st.success("Stable demand pattern detected")
