n = int(input())
a = list(input())
b = len(a)

for i in range(n - 1):
    c = list(input())
    for j in range(b):
        if a[j] != c[j]:
            a[j] = '?'

print(''.join(a))