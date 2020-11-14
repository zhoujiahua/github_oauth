#! /usr/bin/python3

a = 123
b = 456

a, b = b, a

print(a)
print(b)

c = 1

while c < 10:
    c = c + 1
    print('...', c)
