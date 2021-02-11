import sys
a = int(input())
b = []

for i in range(a):
    c, d = sys.stdin.readline().split()
    if d == 'enter':
        b.append(c)
    elif d == 'leave':
        b.remove(c)

b = sorted(b, reverse = True)
for i in b:
    print(i)