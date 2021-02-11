from itertools import combinations

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    a.remove(a[0])
    b = list(combinations(a, 6))
    for i in b:
        print(' '.join(map(str, i)))
    print()

