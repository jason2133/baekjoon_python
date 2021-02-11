a = int(input())
for i in range(1, a+1):
    b = list(map(str, input().split()))
    b[0] = int(b[0])
    b[2] = int(b[2])
    b[4] = int(b[4])
    
    if b[1] == '+':
        if b[0] + b[2] == b[4]:
            print('Case %s: YES' % (i))
        else:
            print('Case %s: NO' % (i))
    else:
        if b[0] - b[2] == b[4]:
            print('Case %s: YES' % (i))
        else:
            print('Case %s: NO' % (i))
        