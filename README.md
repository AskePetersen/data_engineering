## TLDR:
    navigate to the folder where this README.md is, START DOCKER,  and run the following
    commands:
    docker build -t taxi_ingest:v001 .
    Create network if it doesn't already exist:
    docker network create pg-network
    Start a database if you haven't done so already:
        docker run -it `
          -e POSTGRES_USER="root" `
          -e POSTGRES_PASSWORD="root" `
          -e POSTGRES_DB="ny_taxi" `
          -v C:\Users\aske9\OneDrive\data_engineering\ny_taxi_postgres_data `
          -p 5432:5432 `
          --network=pg-network `
          --name pg-database `
          postgres:13

    Then we start pg-admin:
        ```docker run -it `
        -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
        -e PGADMIN_DEFAULT_PASSWORD="root" `
        -p 8080:80 `
        --network=pg-network `
        --name pgadmin `
        dpage/pgadmin4```
    
    We fill the database with data by:
        
        ```
        docker run -it `
        --network=pg-network `
        taxi_ingest:v001 `
            --user=root `
            --password=root `
            --host=pg-database `
            --port=5432 `
            --db=ny_taxi `
            --table_name=ny_taxi `
            --url=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
        ```


### To run docker do:
    docker build -t test:pandas .
    docker run -it test:pandas

### If we want to give the script a command line argument we can do:
    docker run -it test:pandas 14-02-2025

### To start a database:
    docker run -it `
      -e POSTGRES_USER="root" `
      -e POSTGRES_PASSWORD="root" `
      -e POSTGRES_DB="ny_taxi" `
      -v C:\Users\aske9\OneDrive\data_engineering\ny_taxi_postgres_data `
      -p 5432:5432 `
      --network=pg-network `
      --name pg-database `
      postgres:13

### To do pgcli:
    pgcli -h localhost -p 5432 -u root -d ny_taxi
    This starts a connection to the database
    pgcli means postgres command line interface, but one should probably use pgadmin

### To get the taxi dataset:
    wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
    And then in python do:
    df = pd.read_parquet("yellow_tripdata_2021-01.parquet")
    df.to_csv("yellow_tripdata_2021-01.csv")

### PGadmin
    No need to install pgadmin, we can pool it into docker
    ```docker run -it `
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
    -e PGADMIN_DEFAULT_PASSWORD="root" `
    -p 8080:80 `
    --network=pg-network `
    --name pgadmin `
    dpage/pgadmin4```
    This will setup pgadmin in the docker 
    Now we can open our browser and go to localhost:8080
    We create a new server:
        General
            Name: Docker localhost
        Connection:
            Host name/address: pg-database
            Username: root
            password: root

### Creating a network where individual containers can talk with eachother
    ```docker network create pg-network```
