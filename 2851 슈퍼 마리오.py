a = []
c = 0
for i in range(10):
    b = int(input())
    c += b
    a.append(c)

a = sorted(a, reverse=True)
b = []
for i in range(10):
    b.append(abs(100 - a[i]))
    
print(a[b.index(min(b))])
    

