import re

ss = 'life is short, i use python, i love python'

r = re.search('life(.*)python(.*)python', ss)
print(r.group(0, 1, 2))
print(r.groups())
