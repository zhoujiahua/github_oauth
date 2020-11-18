#! /usr/bin/python3

# 枚举类型
from enum import Enum


# 可变
# 防止相同标签的功能
class VIP(Enum):
    # pass
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 枚举类型 枚举的名字 枚举的值
print(VIP.YELLOW)
print(VIP['GREEN'])
print(type(VIP.YELLOW.value), VIP.YELLOW.value)
print(type(VIP.YELLOW.name), VIP.YELLOW.name)

# 枚举遍历
for v in VIP:
    print(v)
