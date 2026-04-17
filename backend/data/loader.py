import pandas as pd
from backend.config import DATA_PATH, LOG_PATH

def load_data():
    df = pd.read_csv(DATA_PATH)
    log_df = pd.read_csv(LOG_PATH)
    return df, log_df

def load_data():
    df = pd.read_csv(DATA_PATH)
    log_df = pd.read_csv(LOG_PATH)
    return df, log_df

