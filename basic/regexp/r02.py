#! /usr/bin/python3

import re

# 正则表达式
a = 'C123C++123Java123Python123Javascript'

r = re.findall('\d{3}', a)
print(r)

for i in range(10):
    print('------', i)

print(len(r))

for v in r:
    print(v)
