list1 = []
dic = {}
list2 = []

entry = input()
n = int(input())

numbers = list(map(int, entry.split()))
for i, num in enumerate(numbers):
    a = n - num
    if a in dic:
        list1.append((dic[a], i))
    dic[num] = i

if not list1:
    print('Not Found!')
else:
    for pair in list1:
        list2.append(pair[0]+pair[1])
    sorted = sorted(list2)
    for u in sorted:
        print(u)
        