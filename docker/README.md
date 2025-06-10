## TLDR:
    navigate to the folder where this README.md is, START DOCKER,  and run the following
    commands. To work you probably have to be in git bash
    run 
        ```
        docker-compose up -d
        ```

    run 
        ```
        docker build -t SOME_NAME .
        ```

    run 
        ```
        URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
        docker run   --network=export_default   SOME_NAME     --user=root     --password=root     --host=pgdatabase     --port=5432     --db=ny_taxi     --table_name=yellow_taxi_trips     --url=${URL}
        ```

### To do pgcli:
    ```
    pgcli -h localhost -p 5432 -u root -d ny_taxi
    ```
    This starts a connection to the database
    pgcli means postgres command line interface, but one should probably use pgadmin

### PGadmin
    No need to install pgadmin, we can pool it into docker
    docker run -it `
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
    -e PGADMIN_DEFAULT_PASSWORD="root" `
    -p 8080:80 `
    --network=pg-network `
    --name pgadmin `
    dpage/pgadmin4
    This will setup pgadmin in the docker 
    Now we can open our browser and go to localhost:8080

### Creating a network where individual containers can talk with eachother
    ```docker network create pg-network```

### Docker Compose
    Utility to have us write less every time we have to start up
    Multiple containers in one file
    We need a docker-compose.yml

_____________________________

### Pay attention to:
    you dont use -it in the docker run command, probably because we use git bash
    host is pgdatabase
    In the run script we use port 5432
    You might have to change the network. It's typically called the same as your
        folder. run ```docker network ls``` to get the available networks
    Remember to be connected to the network.
    pgadmin is at localhost:8080
    There are multiple connection between the 'docker run' and 'docker-compose.yaml'
        script.

To close docker:
    docker-compose down -- You have to be in the correct folder