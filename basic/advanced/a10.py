#! /usr/bin/python3

import time


# 装饰器

def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


def f1():
    print('f1')


f = decorator(f1)
f()
