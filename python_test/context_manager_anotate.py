"""
Context manager Annotation

with 구문 이해
contextlib 데코레이터 사용
"""
import contextlib
import time


# Ex1
# Use decorator
@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f  # __enter__
    f.close()  # __exit__


with my_file_writer("./test4.txt", "w") as f:
    f.write("Context Manager Test4\nContextlib Test4")


# Ex2
# Use decorator
@contextlib.contextmanager
def execute_timer(msg):
    start = time.monotonic()
    try:  # __enter__
        yield start
    except BaseException as e:
        print("Logging exception : {}, {}".format(msg, e))
        raise
    else:  # __exit__
        print("{} : {}s".format(msg, time.monotonic() - start))


with execute_timer("Start Job!") as v:
    print("Received start Monotonic() : {}".format(v))
    # Execute Job
    for i in range(100000000):
        pass

    # raise Error
    # raise Exception("Exception Raised!")
