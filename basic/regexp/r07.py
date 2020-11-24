#! /usr/bin/python3

import re

# 数量词
# * 匹配0次或者无限次
a = '23u98ru9 pythonn this python0 is case python12 qw8eir9iq9324 jerry ir9q&*%$ we0-ir 90qwe python'

print(re.findall('python?', a))

