def select_best_supplier(df):
    df['score'] = (
        0.4 * df['supplier_cost'] +
        0.3 * df['estimated_travel_time'] +
        0.3 * df['CO2_per_km']
    )
    return df.sort_values(by="score").iloc[0].to_dict()