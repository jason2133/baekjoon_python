a, b = map(int, input().split())
c = 1
d = 1

for i in range(a, a-b, -1):
    c = i * c

for i in range(b, 0, -1):
    d = i * d

print(c // d)
