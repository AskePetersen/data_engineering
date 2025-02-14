# selecting python version
FROM python:3.9 

# packages to install. This is done from CLI
RUN pip install pandas 

# The dir we are working from. It's created if it doesn't exists
WORKDIR /app 

# Choose which files are copied from our curr directory on host
COPY pipeline.py pipeline.py 

# Initial commands to run
ENTRYPOINT [ "python", "pipeline.py" ] 
