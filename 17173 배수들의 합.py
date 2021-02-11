a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []
for i in range(1, a+1):
    for j in range(len(c)):
        if i % c[j] == 0:
            d.append(i)

d = set(d)
print(sum(d))