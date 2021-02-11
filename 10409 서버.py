a, b = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
num = 0
for i in range(len(c)):
    if num + c[i] <= b:
        num += c[i]
        ans += 1
    else:
        break

print(ans)        