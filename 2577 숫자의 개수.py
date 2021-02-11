a = int(input())
b = int(input())
c = int(input())

d = a * b * c
e = str(d)
f = list(e)
g = len(f)

n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0

for i in range(0, g):
    if f[i] == '0':
        n0 = n0 + 1

    elif f[i] == '1':
        n1 = n1 + 1

    elif f[i] == '2':
        n2 = n2 + 1

    elif f[i] == '3':
        n3 = n3 + 1

    elif f[i] == '4':
        n4 = n4 + 1

    elif f[i] == '5':
        n5 = n5 + 1

    elif f[i] == '6':
        n6 = n6 + 1

    elif f[i] == '7':
        n7 = n7 + 1

    elif f[i] == '8':
        n8 = n8 + 1

    elif f[i] == '9':
        n9 = n9 + 1

print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)



