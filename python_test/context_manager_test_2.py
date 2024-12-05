"""
Context Manager
Contextlib - Measure execution timer
"""

# Ex1
import time


class ExecuteTimer(object):
    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Logging exception : {}".format((exc_type, exc_val, exc_tb)))
        else:
            print("{} : {}s".format(self.msg, time.monotonic() - self._start))
        return True


with ExecuteTimer("Start Job!") as v:
    print("Received start Monotonic() : {}".format(v))
    # Execute Job
    for i in range(100000000):
        pass

    # raise Error
    raise Exception("Exception Raised!")
