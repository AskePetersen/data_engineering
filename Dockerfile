# selecting python version
FROM python:3.9 

# packages to install. This is done from CLI
RUN apt-get install wget 
RUN pip install pandas sqlalchemy psycopg2 pyarrow

# The dir we are working from. It's created if it doesn't exists
WORKDIR /app 

# Choose which files are copied from our curr directory on host
COPY ingest_data.py ingest_data.py 

# Initial commands to run
ENTRYPOINT [ "python", "ingest_data.py" ] 
