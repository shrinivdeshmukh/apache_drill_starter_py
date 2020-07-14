FROM continuumio/miniconda3

WORKDIR /web

COPY *.py /web/

COPY requirements.txt /web/requirements.txt

RUN apt-get update -y; apt-get install build-essential -y; apt-get install unixodbc-dev -y; pip install -r requirements.txt

CMD ["uvicorn main:app", "--host 0.0.0.0", "--port 80"]
