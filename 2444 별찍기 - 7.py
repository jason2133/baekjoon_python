a = int(input())

for i in range(0, a):
    print((a - i - 1) * ' ' + '*' * (1 + 2 * i))

for i in range(1, a):
     print(' ' * i + '*' * ((-2) * i + 2 * a - 1))



