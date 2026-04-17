import streamlit as st
from components.control_panel import control_panel
from components.simulation import simulate
from components.metrics import show_metrics
from components.forecast import show_forecast
from components.delay import show_delay
from components.inventory import show_inventory
from components.recommendation import show_recommendation
from components.map_view import show_map
from components.optimization import show_optimization
from components.sustainability import show_sustainability
from components.traffic import show_traffic
from components.alerts import show_alerts
from components.decision import show_decision

def dashboard_page():
    st.title("Dashboard")

    col_left, col_right = st.columns([1,3])

    with col_left:
        inputs = control_panel()

    run = inputs["run"]

    if run:
        demand, delay_prob, inventory, reorder = simulate(inputs)

    with col_right:
        show_metrics(run, demand if run else None, delay_prob if run else None)
        show_forecast(run, demand if run else None)
        show_delay(run, delay_prob if run else None)

        colA, colB = st.columns(2)

        with colA:
            show_inventory(run, inventory if run else None, reorder if run else None)

        with colB:
            show_recommendation(run, delay_prob if run else None)

        show_map(run, delay_prob if run else None)
        show_optimization()
        show_sustainability(run)
        show_traffic(run)
        show_alerts(run, delay_prob if run else None, inventory if run else None, reorder if run else None, demand if run else None)
        show_decision(run, delay_prob if run else None, inventory if run else None, reorder if run else None)

