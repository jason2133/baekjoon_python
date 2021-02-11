def jinsu(x:int) -> str:
    d = ''
    dchar = '012345678'
    while x > 0:
        d += dchar[x%9]
        x //= 9
    return d[::-1]

a = int(input())
print(jinsu(a))
    