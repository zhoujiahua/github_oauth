import re

ss = 'A88C1237412D3476'


def convert(value):
    # pass
    mat = value.group()
    if int(mat) >= 6:
        return '9'
    else:
        return '0'


print(re.sub('\d', convert, ss))
