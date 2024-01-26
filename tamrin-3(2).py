import re
list1 = []
n = int(input())
for i in range(n):
    entry = input()
    if '@' in entry:
        result = re.split(r'@', entry)
        list1.append(result[1])
list1 = list(set(list1))
list1.sort()
for h in list1:
    print(h)