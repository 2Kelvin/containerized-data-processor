FROM python:3.14.3-alpine
WORKDIR /csv-processor
RUN pip install pandas==3.0.1
RUN mkdir data-files
COPY processor.py ./
CMD [ "python3", "processor.py" ]