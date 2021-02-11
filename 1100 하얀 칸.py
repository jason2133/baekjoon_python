ans = 0
for i in range(8):
    a = str(input())
    for j in range(8):
        if (i+j) % 2 == 0:
            if a[j] == 'F':
                ans += 1

print(ans)            