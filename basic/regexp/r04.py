#! /usr/bin/python3

import re

# 概括字符集 \d \D \w
a = '23u98ru9 qw8eir9iq9324 ir9q&*%$ we0-ir 90qwe'

print(re.findall('[0-9]', a))
print(re.findall('\w', a))
print(re.findall('\W', a))
print(re.findall('[A-Za-z0-9]', a))
print(re.findall('\s', a))
print(re.findall('\S', a))
