a = str(input())
b = a.upper()
c = ''

for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            if a[i] == '-':
                c = c
            else:
                c = c + a[i]

print(c)


