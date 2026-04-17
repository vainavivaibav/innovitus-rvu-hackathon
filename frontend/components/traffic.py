import streamlit as st
import numpy as np

def show_traffic(run):
    st.subheader("Traffic Insights")

    if run:
        traffic = np.random.randint(50,200,10)
        st.line_chart(traffic)

        if max(traffic) > 180:
            st.warning("High activity detected")
            st.info("Possible demand spike due to traffic surge")
