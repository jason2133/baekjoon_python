while True:
    a = int(input())
    if a == 0:
        break
    b = []
    for i in range(a):
        c = input()
        b.append(c)
       
    d = []
    for i in b:
        d.append(i.lower())
       
    e = sorted(d)
    f = d.index(e[0])
    print(b[f])


