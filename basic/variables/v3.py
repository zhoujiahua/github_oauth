#! /usr/bin/python3

# Variable 变量 语义化 命名规范 系统关键字

# 元祖列表区别
a = [23, 9, 412, 34]  # 可改变类型
b = (23, 4, 1234, 5)  # 不可改变类型
print(id(a))
print(hex(id(a)))

a.append(5)
print(a)

a = (23, 4, 1234, [1, 2, 3, 4])
print(a[3][1])
a[3][1] = 'hi'
print(a[3][1])
