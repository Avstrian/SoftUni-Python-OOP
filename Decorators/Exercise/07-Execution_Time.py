import time


def exec_time(f):
    def wrapper(*args):
        start = time.time()
        result = f(*args)
        end = time.time()
        return end - start

    return wrapper