a, b, c = map(int, input().split())
a1 = 0
a2 = 0

for i in range(a):
    e, f = map(int, input().split())
    if f <= b:
        a2 += 1
    elif e <= b:
        a1 += 1

ans = min(a2, c) * 140       
if a2 < c:
    ans += min(c-a2, a1) * 100

print(ans)            