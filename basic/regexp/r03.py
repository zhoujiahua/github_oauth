#! /usr/bin/python3

import re

# 正则表达式
a = 'abc,acc,adc,aec,afc,ahc'

print(re.findall('a[fc]c', a))
print(re.findall('a[^fc]c', a))
print(re.findall('a[c-f]c', a))
