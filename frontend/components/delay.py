import streamlit as st

import streamlit as st

def show_delay(run, delay):
    st.subheader("Delay Prediction")

    if run:
        if delay >= 85:
            st.error(f"Critical Risk ({delay}%)")
            st.warning("Immediate action required: reroute shipment")

        elif delay >= 70:
            st.error(f"High Risk ({delay}%)")
            st.warning("Consider switching supplier or faster shipping")

        elif delay >= 50:
            st.warning(f"Moderate Risk ({delay}%)")
            st.info("Monitor closely, delays are likely")

        elif delay >= 30:
            st.info(f"Low-Medium Risk ({delay}%)")

        elif delay >= 10:
            st.success(f"Low Risk ({delay}%)")

        else:
            st.success(f"Minimal Risk ({delay}%)")