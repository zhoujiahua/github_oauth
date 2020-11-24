#! /usr/bin/python3

import re

# 数量词
a = '23u98ru9 this is case qw8eir9iq9324 jerry ir9q&*%$ we0-ir 90qwe python'

# 贪婪
print(re.findall('[a-z]{4,6}', a))
# 非贪婪
print(re.findall('[a-z]{4,6}?', a))
