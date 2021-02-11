a = int(input())
b = []
for i in range(a):
    c, d, e, f = map(str, input().split())
    d = int(d)
    e = int(e)
    f = int(f)
    b.append([c, d, e, f])

g = sorted(b, key = lambda x: (-x[1], x[2], -x[3], x[0]))    

for i in range(a):
    print(g[i][0])
