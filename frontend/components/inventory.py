import streamlit as st

def show_inventory(run, inventory, reorder):
    st.subheader("Inventory")

    if run:
        st.write(f"Current: {inventory}")
        st.write(f"Reorder Point: {reorder}")

        if inventory > reorder:
            st.success("Safe")
        elif inventory > reorder*0.7:
            st.warning("Low")
        else:
            st.error("Critical")
