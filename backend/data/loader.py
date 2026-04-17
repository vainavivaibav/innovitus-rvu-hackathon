from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:root@localhost:5432/supplychain",
    pool_pre_ping=True
)

def load_data():
    df = pd.read_sql("SELECT * FROM supply_data", engine)

    try:
        log_df = pd.read_sql("SELECT * FROM access_logs", engine)
    except Exception:
        log_df = pd.DataFrame()

    return df, log_df