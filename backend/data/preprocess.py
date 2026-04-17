import pandas as pd

def preprocess(df):
    df.columns = df.columns.str.strip().str.lower()

    df['order_date_(dateorders)'] = pd.to_datetime(df['order_date_(dateorders)'])
    df['shipping_date_(dateorders)'] = pd.to_datetime(df['shipping_date_(dateorders)'])

    df['order_day'] = df['order_date_(dateorders)'].dt.day
    df['order_month'] = df['order_date_(dateorders)'].dt.month
    df['order_hour'] = df['order_date_(dateorders)'].dt.hour

    df['delay'] = df['days_for_shipping_(real)'] - df['days_for_shipment_(scheduled)']

    return df