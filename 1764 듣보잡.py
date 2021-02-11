a, b = map(int, input().split())
c = []
for i in range(a):
    d = input()
    c.append(d)
d = []
for i in range(b):
    e = input()
    d.append(e)

ans = []
c = set(c)
d = set(d)
for i in c:
    if i in d:
        ans.append(i)

ans = sorted(ans)
print(len(ans))
for i in ans:
    print(i)