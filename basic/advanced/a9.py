#! /usr/bin/python3

# 装饰器
import time


def f1():
    print('f1')


def f2():
    print('f2')


# 开闭原则
def print_current(func):
    print(time.time())
    func()


print_current(f1)
print_current(f2)


