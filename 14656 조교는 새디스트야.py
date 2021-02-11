a = int(input())
b = list(map(int, input().split()))
c = sorted(b)

ans = 0
for i in range(a):
    if b[i] != c[i]:
        ans += 1
print(ans)