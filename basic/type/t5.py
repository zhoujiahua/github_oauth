#! /usr/bin/python3

# Set集合 ==>> 无序
s = {1, 23, 4, 123, 4, 1234, 23}
print({1, 1, 1, 2, 2, 2, 3, 3, 4})
print(len(s))
print(1 in s)
print(1 not in s)
print('差集', {12, 3, 4, 343, 5} - {3, 5})
print('交集', {12, 3, 4, 343, 5} & {3, 5})
print('并集', {12, 3, 4, 343, 5} | {3, 5})
print('定义空集合', type(set()), len(set()))
