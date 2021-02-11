from itertools import product
a, b = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
d = list(product(c, repeat = b))
for i in d:
    print(' '.join(map(str, i)))

