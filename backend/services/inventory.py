import numpy as np

def reorder_point(demand, lead_time, safety_stock):
    return np.mean(demand) * lead_time + safety_stock

def inventory_status(stock, reorder):
    if stock > reorder:
        return "SAFE"
    elif stock > reorder * 0.7:
        return "LOW"
    return "CRITICAL"