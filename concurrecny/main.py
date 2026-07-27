from time import sleep
from sys import getrefcount


def print_hi(name):
    sleep(10)
    print(f"Hello, {name}")


if __name__ == "__main__":
    print_hi("Sara")