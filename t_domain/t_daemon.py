#!/usr/bin/env python
# encoding: utf-8

import time
import os
import daemon
from daemon.pidfile import PIDLockFile

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
path = './this.log'
handler = RotatingFileHandler(path, maxBytes=2000, backupCount=5)
logger.addHandler(handler)

def loop():
    while True:
        print 'Zzz...'
        logger.warn('Zxx...' * 10)
        logger.info('Zxx...' * 10)
        time.sleep(5)


#  out = open('out.log', 'w+')
here = os.path.dirname(os.path.abspath(__file__))


context = daemon.DaemonContext(
    working_directory=here,
    pidfile=PIDLockFile('this.pid'),
     files_preserve = [
         handler.stream
     ],
)

with context:
    loop()
