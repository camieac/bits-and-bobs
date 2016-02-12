#!/usr/bin/env python
from threading import Thread, Semaphore
import sys
import time

INTERVAL = 10

class Worker(Thread):

    def __init__(self, workerSemaphore, processorSemaphore):
        super(Worker, self).__init__()
        self.workerSemaphore    = workerSemaphore
        self.processorSemaphore = processorSemaphore

    def run(self):
        while True:
            # wait for the processor to finish
            self.workerSemaphore.acquire()
            start = time.time()
            while True:
                if time.time() - start > INTERVAL:
                    # wake-up the processor
                    self.processorSemaphore.release()
                    break

                # do work here
                print "I'm working"

class Processor(Thread):
    def __init__(self, workerSemaphore, processorSemaphore):
        super(Processor, self).__init__()
        print "init P"
        self.workerSemaphore    = workerSemaphore
        self.processorSemaphore = processorSemaphore

    def run(self):
        print "running P"
        while True:
            # wait for the worker to finish
            self.processorSemaphore.acquire()
            start = time.time()
            while True:
                if time.time() - start > INTERVAL:
                    # wake-up the worker
                    self.workerSemaphore.release()
                    break

                # do processing here
                print "I'm processing"

workerSemaphore    = Semaphore(1)
processorSemaphore = Semaphore(0)

worker    = Worker(workerSemaphore, processorSemaphore)
processor = Processor(workerSemaphore, processorSemaphore)

worker.start()
processor.start()

worker.join()
processor.join()
