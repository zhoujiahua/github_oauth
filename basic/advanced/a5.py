#! /usr/bin/python3

# map

list_x = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
list_y = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]


def square(x):
    return x * x


# for x in list_x:
#     square(x)

r = map(square, list_x)
print(list(r))

# lambada
rr = map(lambda x: x * x, list_x)
print(list(rr))

rrr = map(lambda x, y: x * x + y, list_x, list_y)
print(list(rrr))
