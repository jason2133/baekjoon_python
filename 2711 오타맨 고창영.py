a = int(input())
for i in range(a):
    b, c = input().split()
    b = int(b)
    print(c[0:b-1], c[b:], sep='')
    
    
    