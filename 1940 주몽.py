a = int(input())
b = int(input())
c = list(map(int, input().split()))
d = 0

for i in range(a):
    for j in range(i+1, a):
        if c[i] + c[j] == b:
            d += 1

print(d)