a = 0
while True:
    b = input()
    a += 1
    if ('E' in b):
        break
    else:
        print('Case %s: %s' % (a, str(eval(b)).lower()))
