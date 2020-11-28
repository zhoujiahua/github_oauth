#! /usr/bin/python3

# Variable 变量 语义化 命名规范 系统关键字
# 运算符
# 值 身份 类型

#  算术运算符
# + - * / // % **
print(1 + 2)
print(2 - 1)
print(5 * 2)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)

# 赋值运算符
# = += -= *= /= %= **= //=
a = 1
a += 1
print(a)

# 比较（关系）运算符 ==>> 值比较
# ==  != > < >= <=
print([1, 2, 3] == [1, 2, 3])
print((1, 2, 3) == (1, 2, 3))
print('a' > 'b')
print('abc' > 'abd')
print(ord('a'))
print(ord('b'))

# 逻辑运算符
# and or not
print(1 and 1)
print(0 or 1)
print(not 1)

# 成员运算符
# in (not in)
print(1 in [23, 4, 23, 1])
print(1 not in (23, 4, 23, 1))
print(1 not in {23, 4, 23, 1})
print('name' in {'name': 'jerry', 'age': 18})

# 身份运算符 ==>> 内存地址比较
# is (is not)
print(1 is 1)
print('abc' is 'adb')
print('abc' is not 'adb')
print(1 is 1.0)
print({1, 2, 3} == {3, 2, 1})  # 集合是无序的
print({1, 2, 3} is {3, 2, 1})
print((1, 2, 3) == (3, 2, 1))  # 元祖是有序的
print((1, 2, 3) is (3, 2, 1))

# 位运算符  （把这个数当做二进制数进行计算） 大概了解用处较少
# & | ^ ~ << >>
# &按位与 |按位或 ^按位异或 ~按位取反 <<左移动 >>右移动
asc = 2
bsc = 3
print(asc & bsc)
print(asc ^ bsc)

# Type 判断
# print(type('abc') == str)  # 不推荐使用
print(isinstance('abd', str))
print(isinstance(123, int))
print(isinstance(1.0, (int, str, float)))
