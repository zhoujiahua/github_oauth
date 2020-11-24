#! /usr/bin/python3

import re

a = -227


def callReset(num):

    # 第一种方式
    # s = re.findall('\D', str(num))
    # n = re.findall('\d', str(num))
    # n.reverse()
    # print(''.join(list(s + n)))

    # 第二种方式
    s = re.findall('.', str(num))
    sn = s[1:len(s)]
    sn.reverse()
    print(''.join(list(s[0]) + list(sn)))


callReset(a)
