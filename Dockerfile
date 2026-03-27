FROM python:3.14.3-alpine
WORKDIR /csv-processor
RUN pip install pandas==3.0.1
RUN mkdir output-folder
COPY processor.py input.csv ./
CMD [ "python3", "processor.py" ]