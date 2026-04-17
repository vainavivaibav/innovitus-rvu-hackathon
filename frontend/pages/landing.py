import streamlit as st

def landing_page():
    def go_dashboard():
        st.session_state.page = "dashboard"

    st.markdown("""
    <div style="text-align:center; padding:50px;">
        <h1>AI Supply Chain Orchestration Platform</h1>
        <p>Predict demand, detect delays, and optimize logistics decisions.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.info("Demand Forecasting")
    col2.info("Delay Prediction")
    col3.info("Route Optimization")
    col4.info("Sustainability Tracking")

    st.button("Launch Dashboard", on_click=go_dashboard)
    st.stop()
