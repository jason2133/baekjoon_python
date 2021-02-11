a = int(input())
b = []
for i in range(a):
    c = list(map(int, input().split()))
    b.append(c)

d = sorted(b, key = lambda x : (-x[2]))
print('%s %s' % (d[0][0], d[0][1]))
print('%s %s' % (d[1][0], d[1][1]))

if d[0][0] == d[1][0]:
    for i in range(2, a):
        if d[i][0] != d[0][0]:
            print('%s %s' % (d[i][0], d[i][1]))
            break
else:
    print('%s %s' % (d[2][0], d[2][1]))

