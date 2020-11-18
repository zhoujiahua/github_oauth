#! /usr/bin/python3

# 函数式编程
# 闭包

def add():
    a = 10

    def cc(x):
        return a * x * x

    return cc


f = add()
print(f(2))
