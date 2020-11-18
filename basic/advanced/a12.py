#! /usr/bin/python3

import time


# 装饰器
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


@decorator
def f1(x):
    print('f1', x)


@decorator
def f2(x, y):
    print('f2', x, y)


# 装饰器语法糖
f1('ok')
f2('hi', 'jerry')
