# celery_worker.py
from __future__ import absolute_import
from celery import Celery

import sys
import configparser
from time import time, sleep

config = configparser.ConfigParser()
config.read('./settings.ini')

brokerServerIP = config['DEFAULT']['BROKER_SERVER_IP']
brokerID       = config['DEFAULT']['BROKER_ID']
brokerPWD      = config['DEFAULT']['BROKER_PASSWORD']

amqp_link = 'amqp://%(id)s:%(password)s@%(host)s' % ({ 'id':brokerID,'password':brokerPWD,'host':brokerServerIP})

app = Celery('celery_tasks', broker=amqp_link, backend=amqp_link)
app.conf.task_reject_on_worker_lost = True
app.conf.task_acks_late             = True

@app.task
def goScanmission(jsonstring):
    result = jsonstring
    print(result)
    print( "JSON Object size : %s bytes" % sys.getsizeof(result) )
    return result

#activate celery
#sh:celery -A celery_tasks worker --loglevel=info