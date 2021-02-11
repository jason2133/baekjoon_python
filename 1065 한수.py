a = int(input())
ans = 0
for i in range(1, a+1):
    if i in range(1, 100):
        ans += 1
    else:
        b = str(i)
        if (int(b[1]) - int(b[0])) == (int(b[2]) - int(b[1])):
            ans += 1
            
print(ans)    