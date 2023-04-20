import time
import hashlib
import re

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic
from pika.spec import BasicProperties
from server import channel


def process_msg(chan: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    log = body.decode("utf-8") #interpréter body en utf-8
    id = hashlib.md5(log.encode('utf-8')).hexdigest() #librairie hashlib pour réencoder
    my_regex = "(\d+.\d+.\d+.\d+) (\S+) (\S+) \[([^\]]+)\] *" #extraire timestamp avec un regex, chaque groupe entre()
    p = re.compile(my_regex)
    m = p.match(log) #contient tous les groupes
    timestamp = m.group(4) #appelle groupe 4
    with open("data_lake.csv", "a") as file:    #ouvre fichier csv
        line = id + ";" + timestamp + ";" + log  #définit ligne
        file.write(id + ";" + timestamp + ";" + log)   #crée ligne ds fichier

# consume messages from queues
def consume():
    channel.basic_consume(queue="queue-data-lake", on_message_callback=process_msg, auto_ack=True)
    channel.start_consuming()
