import argparse
import os

import pandas as pd
from sqlalchemy import create_engine

csv_name = "output.csv"


engine = create_engine(f"postgresql://root:root@localhost:5432/root")
engine.connect()

df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
df = pd.read_csv(csv_name)
df.head(n=0).to_sql(name="ny_taxi", con=engine, if_exists="replace")

while True:
    try:
        df = next(df_iter)
    except:
        print("done")
        break

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name="ny_taxi", con=engine, if_exists="append")

    print("inserted another chunk")
