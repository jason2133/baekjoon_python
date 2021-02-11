from itertools import combinations
a, b = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
d = list(combinations(c, b))
e = []
for i in d:
    e.append(i)
e = sorted(list(set(e)))

for i in e:
    for j in i:
        print(j, end = ' ')
    print()    


