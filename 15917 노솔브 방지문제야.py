import sys
a = int(input())
for i in range(a):
    b = int(sys.stdin.readline().strip())
    c = bin(b)
    if c.count('1') == 1:
        print(1)
    else:
        print(0)
