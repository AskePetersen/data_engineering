import argparse
import os

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = 'output.csv'
    os.system(f"curl {url} -OutFile 123")
    print(1)
    parquet_name = url.split('/')[-1]
    df = pd.read_parquet(parquet_name)
    print(2)
    df.to_csv(csv_name, index=False)
    print(3)


    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    print(4)
    engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    df.to_sql(name=table_name, con=engine, if_exists="append")
    while True:
        try:
            df = next(df_iter)
        except:
            print("done")
            break

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists="append")

        print("inserted another chunk")
        break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    parser.add_argument("--user", help="username for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument("--table_name", help="name of the table where we write results")
    parser.add_argument("--url", help="url of the csv file")

    args = parser.parse_args()

    main(args)
