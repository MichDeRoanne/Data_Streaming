# Project Data Streaming

The aim of this project is to process logs from an Nginx server.

The logs will be processed via a route that includes a producer and two consumers, which will insert the processed and cleaned logs into specific tables in the database.


## Required

* Python
* Docker


## Install

Execute:

```console
git clone https://github.com/MichDeRoanne/Project_RabbitMQ
```

```console
python -m venv venv
```

```console
pip install -r requirements.txt
```


## Docker

The docker-compose file will create the containers RabbitMQ.


## Build and run the Docker image: :

Execute:

```console
docker-compose up -d
```


## Logs producer

To produce the events, run the file **'logsproducer.py'**


## Data_lake_consumer

To consume the events from the data-lake route, run the file **'data_lake_consumer.py'**


## Data-clean-consumer

To consume the events from the data-clean route, run the file **'data-clean-consumer.py'**
