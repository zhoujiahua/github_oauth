import re

a = 'abcasdasabcadsfasdaabcabcafdsdfsdfsabc'
print(re.findall('abc', a))
print(re.sub('abc', 'jerry', a))
print(re.sub('abc', 'jerry', a, 1))
print(a.replace('abc', 'Tom'))


def convert(value):
    # pass
    print(value)
    mat = value.group()
    return '!!' + mat + '!!'


print(re.sub('abc', convert, a))
