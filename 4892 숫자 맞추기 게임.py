i = 1
while True:
    a0 = int(input())
    a1 = 3*a0
    if a0 == 0:
        break
    if a1 % 2 == 0:
        print('%s. even %s' % (i, a0//2))
        i += 1
    else:
        print('%s. odd %s' % (i, (a0-1)//2))
        i += 1
    