a = str(input())

# 8진수
if a[0] == '0' and a[1] != 'x' :
    b = int(a, 8)
    print(b)

# 10 진수
if a[0] != '0':
    b = a
    print(b)

# 16진수
if a[0] == '0' and a[1] == 'x':
    b = int(a, 16)
    print(b)





