import threading
import time


class TaskThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Flag to pause thread
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())

    def run(self):
        i = 0
        while i < 100:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()

                # thread should do the thing if
                # not paused
                print 'do the thing'
                i += 1
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

if __name__ == "__main__":
    t = TaskThread()

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

    print "Waiting for termination"
    t.join()

    print "Done"
