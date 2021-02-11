a, b = map(int, input().split())
c = [i for i in range(1, a+1)]
for i in range(b):
    d, e = map(int, input().split())
    c[d-1], c[e-1] = c[e-1], c[d-1]

for i in c:
    print(i, end = ' ')
