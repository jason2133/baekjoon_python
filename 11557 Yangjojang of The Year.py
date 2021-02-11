a = int(input())
for i in range(a):
    b = int(input())
    c = []
    
    for j in range(b):
        d, e = map(str, input().split())
        e = int(e)
        c.append([d, e])
        
    c = sorted(c, key = lambda x : (-x[1]))
    print(c[0][0])