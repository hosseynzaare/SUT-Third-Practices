import re
arg = input()
b = re.findall('([a-z0-9A-Z\^/?#()\[$@}|%{\]/s{+-><"\\\':;_=*\\\&^!]{1})([0-9]+)', arg)
b.sort(key=lambda x: int(x[1]))
text = [x[0] for x in b]
print(''.join(text))