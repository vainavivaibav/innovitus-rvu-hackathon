def make_decision(demand, delay, inventory_state):
    if delay == 1:
        return "Switch supplier or route"
    if inventory_state != "SAFE":
        return "Reorder stock"
    return "Operations normal"