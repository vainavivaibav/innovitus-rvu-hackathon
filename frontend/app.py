import streamlit as st
from pages.landing import landing_page
from pages.dashboard import dashboard_page

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "landing"

if st.session_state.page == "landing":
    landing_page()
else:
    dashboard_page()
