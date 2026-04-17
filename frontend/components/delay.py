import streamlit as st

def show_delay(run, delay):
    st.subheader("Delay Prediction")

    if run:
        if delay > 70:
            st.error(f"High Risk ({delay}%)")
            st.warning("Switch to faster shipping mode")
        elif delay > 50:
            st.warning(f"Medium Risk ({delay}%)")
        else:
            st.success(f"Low Risk ({delay}%)")
