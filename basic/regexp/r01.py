#! /usr/bin/python3

import re

# 正则表达式
a = 'C|C++|Java|Python|Javascript'

print(a.index('Python'))
print(re.findall('Python', a))
print(re.findall('PHP', a))

# 规则
