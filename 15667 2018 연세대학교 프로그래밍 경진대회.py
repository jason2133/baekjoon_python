a = int(input())
a = a - 1
for i in range(1, a):
    if i*(i+1) == a:
        b = i
        break
print(b)