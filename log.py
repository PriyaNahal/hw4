import time

def timestamp(func):
    def wrapper():
        latest_time = time.ctime()
        print(latest_time)
        func()
    return wrapper


