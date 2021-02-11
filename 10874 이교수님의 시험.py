a = int(input())
num = []
for i in range(1, a+1):
    b = list(map(int, input().split()))
    for j in range(10):
        ans = ((j) % 5) + 1
        if b[j] != ans:
            num.append(i)
            break
           
for i in range(1, a+1):
    if i in num:
        pass
    else:
        print(i)