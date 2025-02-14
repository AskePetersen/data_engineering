### To run docker do:
    docker build -t test:pandas .
    docker run -it test:pandas

### If we want to give the script a command line argument we can do:
    docker run -it test:pandas 14-02-2025

### To start a database:
    docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v C:\Users\aske9\OneDrive\data_engineering\ny_taxi_postgres_data -p 5432:5432 postgres:13

### To do pgcli:
    pgcli -h localhost -p 5432 -u root -d ny_taxi
    This starts a connection to the database
    pgcli means postgres command line interface

### To get the taxi dataset:
    wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
    And then in python do:
    df = pd.read_parquet("yellow_tripdata_2021-01.parquet")
    df.to_csv("yellow_tripdata_2021-01.csv")


