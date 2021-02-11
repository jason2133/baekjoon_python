# 이거 너무 큰 숫자라서 log를 적용해서 풀어야 되네
# 수학적인 요소가 가미된.. 아주..ㅎ^^

a, b = map(int, input().split())
c = 1
d = 1

for i in range(a, a-b, -1):
    c = i * c

for i in range(b, 0, -1):
    d = i * d

print((c // d) % 1000000007)