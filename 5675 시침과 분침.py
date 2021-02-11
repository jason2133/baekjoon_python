import sys
for i in sys.stdin:
    if int(i) % 6 == 0:
        print('Y')
    else:
        print('N')
