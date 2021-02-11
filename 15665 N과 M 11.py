from itertools import product
a, b = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
d = list(product(c, repeat=b))
e = []
for i in d:
    e.append(i)

e = sorted(list(set(e)))    

for i in e:
    for j in i:
        print(j, end = ' ')
    print()
