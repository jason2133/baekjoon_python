a = input()
b0 = 0
b1 = 0

if a[0] == '1':
    b0 += 1
else:
    b1 += 1
    
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        if a[i+1] == '1':
            b0 += 1
        else:
            b1 += 1

print(min(b0, b1))