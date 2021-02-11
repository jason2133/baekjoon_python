from collections import Counter

a = int(input())
b = []
for i in range(a):
    c = input()
    b.append(c)
b = sorted(b)
    
d = Counter(b).most_common()
print(d[0][0])
