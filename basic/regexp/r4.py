import re

ss = 'life is short,i use python'

r = re.search('life(.*)python', ss)
print(r.group(0))
print(r.group(1))
print(re.findall('life(.*)python', ss))
