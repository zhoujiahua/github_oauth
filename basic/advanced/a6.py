#! /usr/bin/python3

# reduce
from functools import reduce

list_x = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
list_y = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]

# 连续计算，连续调用lambda
r = reduce(lambda x, y: x + y, list_x)
print(r)

rr = reduce(lambda x, y: x + y, list_x, 10)
print(rr)

# map/reduce 编程模型 映射 归约 并行计算
