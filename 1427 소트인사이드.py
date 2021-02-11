a = str(input())

b = sorted(a, reverse=True)

c = ''

for i in range(len(b)):
    c = c + b[i]

print(c)