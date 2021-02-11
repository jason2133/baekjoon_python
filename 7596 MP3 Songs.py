i = 1
while True:
    a = int(input())
    if a == 0:
        break
    b = []
    for j in range(a):
        c = str(input())
        b.append(c)
       
    d = sorted(b)
    print(i)
    i += 1
    for k in d:
        print(k)
    