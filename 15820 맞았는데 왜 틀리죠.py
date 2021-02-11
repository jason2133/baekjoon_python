n, m = map(int, input().split())
for i in range(n+m):
    l = input().split()
    if (l[0] != l[1]): print('Wrong Answer' if i < n else 'Why Wrong!!!'); break
else: print('Accepted')

