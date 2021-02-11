a = int(input())
for i in range(a):
    b = int(input())
    c = []
    for j in range(b):
        d, e = map(int, input().split())
        c.append([d, e])
    c = sorted(c, key=lambda x : x[1])
    f = []
    for k in range(b):
        f.append((c[k][1] / c[k][0]))
    g = f.index(min(f))
    print(c[g][1])
    
    