#! /usr/bin/python3

# 装饰器优化 AOP思想
import time


# 装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        print(time.time())
        func(*args, **kwargs)

    return wrapper


@decorator
def f0():
    print('f0')


@decorator
def f1(x):
    print('f1', x)


@decorator
def f2(x, y):
    print('f2', x, y)


@decorator
def f3(x, y, **kwargs):
    print('f3', x, y, kwargs)


# 装饰器语法糖
f0()
f1('hi')
f2('hi', 'jerry')
f3('hi', 'tom', a=1, b=2, c=3)
