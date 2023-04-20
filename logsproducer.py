import re


class Log:
    def __init__(self):
        self.ip = None
        self.user = None
        self.is_email = None
        self.status = None
        self.status_verbose = None

    def parse(self, line: str):
        # print(f"parsing --> {line}")
        regex = re.compile(r"(?P<ip>\S{7,15}) (?P<session>\S{1}|\S{15}) (?P<user>\S{1,50}) \[(?P<timestamp>\S{20}) "
                           r"(?P<utc>\S{5})\] \"(?P<method>GET|POST|DELETE|PATCH|PUT) (?P<url>\S{1,4096}) "
                           r"(?P<version>\S{1,10})\" (?P<status>\d{3}) (?P<size>\d+) -")
        match = re.search(regex, line)
        self.ip = match.group("ip")
        self.user = match.group("user")
        self.status = match.group("status")


import time

from server import channel

QUEUES = [
    {
        "name": "queue-data-lake",
        "topic": "logs"
    },
    {
        "name": "queue-data-clean",
        "topic": "logs"
    }
]

EXCHANGE_NAME = "topic-exchange"

# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')

# create queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['topic'])

# publish line to queue
def publish_event(line):
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key="logs", body=line)
    print(line)
