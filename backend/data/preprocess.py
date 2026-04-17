import pandas as pd

def preprocess(df):
    df = df.fillna(0)

    df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'])
    df['shipping date (DateOrders)'] = pd.to_datetime(df['shipping date (DateOrders)'])

    df['order_day'] = df['order date (DateOrders)'].dt.day
    df['order_month'] = df['order date (DateOrders)'].dt.month
    df['order_hour'] = df['order date (DateOrders)'].dt.hour

    df['delay'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']

    return df