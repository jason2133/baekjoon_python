a, b = map(int, input().split())

ans = (str(a//b) + '.')
a = (a % b) * 10

for i in range(1000):
    ans += str(a // b)
    a = (a % b) * 10
   
print(ans)
