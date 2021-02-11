a, b = map(int, input().split())
c = []
for i in range(a):
    d = input()
    c.append(d)
    
c = sorted(c)
print(c[b-1])

