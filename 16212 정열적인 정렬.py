a = int(input())
b = list(map(int, input().split()))
b = sorted(b)
for i in b:
    print(i, end = ' ')