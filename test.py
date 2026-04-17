from sqlalchemy import create_engine
import pandas as pd
import psycopg2

engine = create_engine("postgresql://postgres:root@localhost:5432/supplychain")


pd.concat([
    pd.read_csv("database/dataset1.csv"),
    pd.read_csv("database/dataset2.csv"),
    pd.read_csv("database/dataset3.csv")
]).to_sql("supply_data", engine, if_exists='append', index=False)

print("All 3 CSVs uploaded successfully ✅")