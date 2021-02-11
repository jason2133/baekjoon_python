from collections import Counter

a = int(input())
b = []
for i in range(a):
    c = str(input())
    b.append(c)
b = sorted(b, reverse=True)
d = Counter(b).most_common()
print('%s %s' % (d[0][0], d[0][1]))



