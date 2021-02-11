a = list(map(int, input().split()))

d = 0
e = 0

# a 구역
for i in range(0, 4):
    if a[i] == 1:
        d = d + 1
    elif a[i] == 0:
        e = e + 1

if d == 3 :
    print("A")

elif d == 2 :
    print("B")

elif d == 1 :
    print("C")

elif e == 4:
    print("D")

elif d == 4:
    print("E")