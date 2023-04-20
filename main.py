# from log import Log
# from transformations import UserTransformation, StatusCodeTransformation
from logsproducer import publish_event
import sys

import data_lake_consumer


def log_producer():
    with open("assets/web-server-nginx.log") as file:
        for line in file:
            # log = Log()
            # log.parse(line)
            # log = StatusCodeTransformation().transform(log)
            # print(f"{log.status} {log.status_verbose}")
            publish_event(line)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Possible arguments: producer, consumer-lake, consumer-clean")
    else:
        arg = sys.argv[1]
        if arg == "producer":
            log_producer()
        elif arg == "consumer-lake":
            data_lake_consumer.consume()
        else:
            print("Unexpected argument")

