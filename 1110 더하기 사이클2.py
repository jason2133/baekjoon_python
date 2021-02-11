a = b = int(input())
ans = 0

while True:
    c = a // 10
    d = a % 10
    e = c + d
    a = d*10 + e%10
    ans += 1
    if a == b:
        break

print(ans)


