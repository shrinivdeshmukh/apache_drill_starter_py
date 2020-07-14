FROM openjdk:8 AS java

RUN apt-get update -y

FROM continuumio/miniconda3

RUN apt-get update -y; apt-get install build-essential -y; apt-get install unixodbc-dev -y

COPY requirements.txt /work/

RUN pip install -r /work/requirements.txt

COPY example.ipynb /work

COPY --from=java /usr/local/openjdk-8 /usr/local/openjdk-8

COPY drill-jdbc-all-1.17.0.jar /opt/conda/lib/python3.7/site-packages/pyspark/jars/

ENV JAVA_HOME=/usr/local/openjdk-8

WORKDIR /work

CMD jupyter notebook --ip=0.0.0.0 --allow-root