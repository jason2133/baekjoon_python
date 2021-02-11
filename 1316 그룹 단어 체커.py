a = int(input())
ans = 0

for i in range(a):
    b = input()
    for j in range(len(b)):
        if j != len(b) - 1:
            if b[j] == b[j+1]:
                pass
            elif b[j] in b[j+1:]:
                break
        else:
            ans += 1
print(ans)