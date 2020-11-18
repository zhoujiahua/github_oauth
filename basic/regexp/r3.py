import re

ss = 'A88C1237412D3476'

print(re.match('\d', ss))
print(re.search('\d', ss))
print(re.findall('\d{3}', ss))
