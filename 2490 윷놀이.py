a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = 0
e = 0

f = 0
g = 0

h = 0
k = 0

# a 구역
for i in range(0, 4):
    if a[i] == 1:
        d = d + 1
    elif a[i] == 0:
        e = e + 1

if d == 3:
    print("A")

elif d == 2:
    print("B")

elif d == 1:
    print("C")

elif e == 4:
    print("D")

elif d == 4:
    print("E")

# b 구역
for i in range(0, 4):
    if b[i] == 1:
        f = f + 1
    elif b[i] == 0:
        g = g + 1

if f == 3 :
    print("A")

elif f == 2 :
    print("B")

elif f == 1 :
    print("C")

elif g == 4:
    print("D")

elif f == 4:
    print("E")

# c 구역
for i in range(0, 4):
    if c[i] == 1:
        h = h + 1
    elif c[i] == 0:
        k = k + 1

if h == 3 :
    print("A")

elif h == 2 :
    print("B")

elif h == 1 :
    print("C")

elif k == 4:
    print("D")

elif h == 4:
    print("E")
