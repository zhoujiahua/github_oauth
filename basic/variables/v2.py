#! /usr/bin/python3

# Variable 变量 语义化 命名规范 系统关键字

# 值类型
a = 1
b = a
a = 12
print(a)
print(b)

# 引用类型
aa = [1, 2, 3, 4, 5]
bb = aa
aa[0] = 99
print(aa)
print(bb)

print(id(a))
