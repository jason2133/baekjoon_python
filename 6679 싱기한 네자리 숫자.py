def jinsu(x, y):
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x != 0:
        d += dchar[x % y]
        x //= y
    return d[::-1]

for i in range(1000, 10000):
    # 10진수
    num = i
    a = 0
    while num != 0:
        a += (num % 10)
        num //= 10
       
    # 12진수
    num = i
    b = 0
    while num != 0:
        b += (num % 12)
        num //= 12
    
    # 16진수
    num = i
    c = 0
    while num != 0:
        c += (num % 16)
        num //= 16
    
    if a == b == c:
        print(i)
    