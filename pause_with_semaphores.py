#!/usr/bin/env python
from threading import Thread, Semaphore
import sys
import time

INTERVAL = 10
class Task():
    def __init__(self):
        self.counter = 0
        self.max_counter = 10

    def oneIteration(self):
        self.counter += 1

    def terminationCase(self):
        return self.counter == self.max_counter


class TaskScheduler(Thread):

    def __init__(self, task_semaphore, task):
        super(Worker, self).__init__()
        self.task_semaphore = task_semaphore

    def run(self):
        while True:
            # Wait for the semaphore to release
            self.task_semaphore.acquire()
            while True:
                if task.terminationCase():
                    # Exit the task scheduler
                    break

                if task.pauseCase() or 

                task.oneIteration()


# Initialise worker semaphore with 1, so we run right away
task_semaphore = Semaphore(1)


task_scheduler = TaskScheduler(task_semaphore)

task_scheduler.start()

task_semaphore.acquire()

task_scheduler.join()
