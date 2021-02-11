a = []
b = []
for i in range(3):
    c = int(input())
    a.append(c)
   
for i in range(3):
    d = int(input())
    b.append(d)
   
a1 = a[0] * 3 + a[1] * 2 + a[2] * 1
b1 = b[0] * 3 + b[1] * 2 + b[2] * 1

if a1 == b1:
    print('T')
elif a1 > b1:
    print('A')
elif a1 < b1:
    print('B')
