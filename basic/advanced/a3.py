#! /usr/bin/python3

# 匿名函数
# lambada 表达式

def add_sum(x, y):
    return x + y


print(add_sum(2, 5))

f = lambda x, y: x + y
print(f(10, 2))
