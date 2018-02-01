# master.py
from __future__ import absolute_import
import json
import sys
import celery_tasks as c
from time import time, sleep

tasks_start = time()

tasks = []

N = 10

jsonSample = json.loads(open('./sample-generated.json').read())

#json_string = jsonSample
json_string = json.dumps(jsonSample)

print( "JSON Object size : %s bytes" % len(json_string))
#print( "JSON Object size : %s bytes" % sys.getsizeof(json_string) )

message_count = 0 

for k in range(N):
    #print(json_string)
    tasks.append(c.goScanmission.delay(json_string))
    message_count = message_count + 1

print('Message Count : ' + str(message_count))

ready= []

collect_start = time()

for k, t in enumerate(tasks):
    response = t.wait()
    ready.append(response)

done = time()

print('celery', collect_start - tasks_start, done - tasks_start)