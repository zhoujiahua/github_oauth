#! /usr/bin/python3

# 

counter = 0

while counter <= 10:
    counter += 1
    print('Hi ..........')
else:
    print('EOF')

a = [12,34,23,4,123,41]
for x in a:
    print(x)

for j in range(0,10,2):
    print(j, end = ' | ')

b = [1,2,3,4,5,6,7,8,9]
c = b[0:len(b):2]
print('------',c)