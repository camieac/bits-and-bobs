import threading
import time
from tiberius.control_api.task import Task


class TaskThread(threading.Thread):
    def __init__(self, task):
        threading.Thread.__init__(self)
        # Flag to pause thread
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())

        # Store a copy of the task to be executed
        self.task = task

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    task.onPause()
                    self.pause_cond.wait()


                # thread should do the thing if
                # not paused
                task.oneIteration()
                # If the task becomes in a completed state, exit
                if task.terminationCase():
                    break
            time.sleep(0.1)

    def pause(self):
        self.paused = True
        # If in sleep, we acquire immediately, otherwise we wait for thread
        # to release condition. In race, worker will still see self.paused
        # and begin waiting until it's set back to False
        self.pause_cond.acquire()

    # should just resume the thread
    def resume(self):
        self.paused = False
        # Notify so thread will wake after lock released
        self.pause_cond.notify()
        # Now release the lock
        self.pause_cond.release()


class TestTask(Task):
    def __init__(self):
        super(TestTask, self).__init__()
        self.task_name = 'Drive Forwards Until Wall'
        self.task_id = 0
        self.task_description = '''Drive forwards at half speed until a wall
                is sensed using the ultrasonics with a
                distance of 10cm.'''

        self.__counter = 0

    def oneIteration(self):
        self.__counter += 1
        print "Doing the task! ", int(self.__counter)
        time.sleep(0.2)

    def terminationCase(self):
        return self.__counter == 30

    def onPause(self):
        print "We are paused."

    def pauseTask(self):
        self.control.stop()

    def resumeTask(self):
        self.runTask()

if __name__ == "__main__":
    task = TestTask()
    t = TaskThread(task)

    print "Starting thread"
    t.start()

    print "Waiting 1s"
    time.sleep(1)

    print "Pausing thread"
    t.pause()

    print "Waiting 1s"
    time.sleep(1)

    print "Resuming thread"
    t.resume()

    print "Waiting 1s"
    time.sleep(1)

    print "Pausing thread"
    t.pause()

    print "Waiting 1s"
    time.sleep(1)

    print "Resuming thread"
    t.resume()

    print "Waiting for termination"
    t.join()

    print "Done"
