import pandas as pd
from xgboost import XGBRegressor, XGBClassifier

def train_models(df):

    features_demand = [
        'order_day',
        'order_month',
        'order_hour',
        'sales_per_customer',
        'category_id',
        'customer_segment'
    ]

    X_demand = pd.get_dummies(df[features_demand])
    y_demand = df['order_item_quantity']

    demand_model = XGBRegressor(n_estimators=50)
    demand_model.fit(X_demand, y_demand)

    features_delay = [
        'days_for_shipment_(scheduled)',
        'shipping_mode',
        'order_region',
        'order_status',
        'latitude',
        'longitude'
    ]

    X_delay = pd.get_dummies(df[features_delay])
    y_delay = df['late_delivery_risk']

    delay_model = XGBClassifier()
    delay_model.fit(X_delay, y_delay)

    return demand_model, delay_model, X_demand.columns, X_delay.columns