a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

a3 = a2
b3 = a3 - b1 + b2
c3 = b3 - c1 + c2
d3 = c3 - d1 + d2

k = max(a3, b3, c3, d3)

print(k)


