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


@decorator
def f2():
    print('f2')


f = decorator(f1)
f()

# 装饰器语法糖
f2()
