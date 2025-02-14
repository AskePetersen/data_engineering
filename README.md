To run docker do:
    docker build -t test:pandas .
    docker run -it test:pandas

If we want to give the script a command line argument we can do:
    docker run -it test:pandas 14-02-2025
