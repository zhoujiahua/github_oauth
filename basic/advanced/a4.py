#! /usr/bin/python3

# 匿名函数
# lambada 表达式
# 三元表达式

def add_sum(x, y):
    return x + y


print(add_sum(2, 5))

f = lambda x, y: x + y
print(f(10, 2))

x, y = 1, 2
c = x if x > y else y
print(c)
