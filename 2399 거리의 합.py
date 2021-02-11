a = int(input())
b = list(map(int, input().split()))
c = 0

for i in range(a-1):
    for j in range(i+1, a):
        c += abs(b[i] - b[j])

print(c*2)        