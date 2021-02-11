from itertools import combinations_with_replacement

a, b = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
d = list(combinations_with_replacement(c, b))
for i in d:
    print(' '.join(map(str, i)))


