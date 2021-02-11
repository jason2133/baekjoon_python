from itertools import permutations

a = int(input())
b = [i for i in range(1, a+1)]
c = list(permutations(b, a))
c = sorted(c)
for i in c:
    for j in i:
        print(j, end = ' ')
    print()
