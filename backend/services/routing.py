def route_info(row):
    return {
        "distance": row['distance_km'],
        "time": row['estimated_travel_time'],
        "traffic": row['traffic_condition']
    }