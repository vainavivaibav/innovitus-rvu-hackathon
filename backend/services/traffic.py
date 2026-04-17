import pandas as pd

def detect_spike(log_df):
    try:
        if "timestamp" not in log_df.columns:
            return "Traffic data not available"

        log_df['timestamp'] = pd.to_datetime(log_df['timestamp'])
        log_df['hour'] = log_df['timestamp'].dt.hour

        hits = log_df.groupby('hour').size()

        if hits.max() > 100:
            return "High traffic detected → demand may increase"

        return "Traffic normal"

    except:
        return "Traffic analysis failed"