a = int(input())
b = list(map(int, input().split()))
b = sorted(b)

if a % 2 == 1:
    print(b[a//2])
else:
    print(b[a//2 - 1])
