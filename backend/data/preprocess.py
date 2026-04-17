import pandas as pd

def preprocess(df):

    df.columns = df.columns.str.strip().str.lower()

    df['order_date_(dateorders)'] = pd.to_datetime(
        df['order_date_(dateorders)'], errors='coerce'
    )
    df['shipping_date_(dateorders)'] = pd.to_datetime(
        df['shipping_date_(dateorders)'], errors='coerce'
    )

    df['order_day'] = df['order_date_(dateorders)'].dt.day.fillna(0)
    df['order_month'] = df['order_date_(dateorders)'].dt.month.fillna(0)
    df['order_hour'] = df['order_date_(dateorders)'].dt.hour.fillna(0)

    df['delay'] = (
        df['days_for_shipping_(real)'] - df['days_for_shipment_(scheduled)']
    ).fillna(0)

    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    categorical_cols = df.select_dtypes(include=['object']).columns
    df[categorical_cols] = df[categorical_cols].fillna("unknown")

    return df