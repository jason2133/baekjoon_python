import sys

n = int(input())

for i in range(n):
    arr = sys.stdin.readline().split()
    print(int(arr[0]) + int(arr[1]))


