def jinsu(x, r):
    dchar = '0123456789ABCDEF'
    if x < r:
        return str(dchar[x])
    else:
        return jinsu(x//r, r) + str(dchar[x%r])

a, b = map(int, input().split())
k = jinsu(a, b)
print(k)