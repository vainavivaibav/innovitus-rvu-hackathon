import pandas as pd
from xgboost import XGBRegressor, XGBClassifier

def train_models(df):

    # Demand model
    features_demand = [
        'order_day','order_month','order_hour',
        'Sales per customer','Category Id','Customer Segment'
    ]

    X_demand = pd.get_dummies(df[features_demand])
    y_demand = df['Order Item Quantity']

    demand_model = XGBRegressor(n_estimators=50)
    demand_model.fit(X_demand, y_demand)

    # Delay model
    features_delay = [
        'Days for shipment (scheduled)',
        'Shipping Mode','Order Region','Order Status',
        'Latitude','Longitude'
    ]

    X_delay = pd.get_dummies(df[features_delay])
    y_delay = df['Late_delivery_risk']

    delay_model = XGBClassifier()
    delay_model.fit(X_delay, y_delay)

    return demand_model, delay_model, X_demand.columns, X_delay.columns