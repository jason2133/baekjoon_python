a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    d = sum(c)
    if d == 0:
        print('Equilibrium')
    elif d > 0:
        print('Right')
    else:
        print('Left')

