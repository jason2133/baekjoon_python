a = int(input())
b = list(map(int, input().split()))

y = 0
m = 0

for i in b:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15

if y > m:
    print('M %s' % m)
elif y < m:
    print('Y %s' % y)
elif y == m:
    print('Y M %s' % y)



