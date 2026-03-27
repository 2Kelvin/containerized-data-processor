# Containerized Data Processor
Docker containerized program that processes a CSV file and outputs the result in a text file that a user can access in the host OS.

Building image:
```bash
docker build -t rocketman02/csv-processor-python:v1 .
```

Running container:
```bash
docker run --rm --mount type=bind,source=$HOME/docker-containers-volumes-data/csv-program,target=/csv-processor/data-files rocketman02/csv-processor-python:v1
```

Used `bind mount` to mount and bind a host folder `$HOME/docker-containers-volumes-data/csv-program` to the  `/csv-processor/data-files` container folder. This way the program running in the container could access and fetch the csv file located in the user's pc and the user could get the output file that the program spits out after processing the csv file.