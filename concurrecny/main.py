import time
from time import sleep
from sys import getrefcount
import threading
from functools import partial

import requests


# def print_hi(name):
#     sleep(10)
#     print(f"Hello, {name}")


def worker(number):
    start = time.time()
    sleep(2)
    print(f"worker {number}, start at {start}, finished {time.time()} .")

def get_page(url):
    try:
        response = requests.get(url)
    except:
        print(f"Error occurred {url}")
    print(f"get completed {url}")



if __name__ == "__main__":

    links = [
        "https://7learn.ac",
        "https://google.com",
    ] *4
    # print_hi("Sara")

    # for i in range(5):
    #     worker(i)
    # for i in range(4):
    #     t = threading.Thread(target= worker, args = (i,))
    #     t.start()

    threads =list()

    for link in links:
        t = threading.Thread(target = get_page, args = (link, ))
        t.setDaemon(True)

        threads.append(t)
        t.start()

    print("threads not joined yet.")

    for tr  in threads:
        tr.join()

    print("All threads hae done")