import sys

a = sys.stdin.readline()

for Repeat in range(0, int(a)):
    b = sys.stdin.readline().split()
    print(int(b[0]) + int(b[1]))
