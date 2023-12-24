#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
    sys.stdout.write('213.234.105.208 - [2023-12-24 10:01:01.689761] "GET /projects/260 HTTP/1.1" yam 972\n')
    sys.stdout.flush()
