a, b = map(int, input().split())
mile = []
for i in range(a):
    c, d = map(int, input().split())
    e = list(map(int, input().split()))
    e = sorted(e, reverse = True)
    if c < d:
        mile.append(1)
    elif c == d:
        mile.append(e[-1])
    elif c > d:
        mile.append(e[d-1])

mile = sorted(mile)
num = 0
ans = 0
for i in range(len(mile)):
    if num + mile[i] <= b:
        ans += 1
        num += mile[i]
print(ans)            