a = int(input())

if a % 5 == 0:
    print(a // 5)

elif a % 5 == 3:
    print(a // 5 + 1)

elif a // 5 - 1 >= 0 and a - (5 * (a // 5 - 1)) == 6:
    print((a // 5 - 1) + 2)

elif a // 5 - 1 >= 0 and a - (5 * (a // 5 - 1)) == 9:
    print((a // 5 - 1) + 3)

elif a // 5 - 2 >= 0 and a - (5 * (a // 5 - 2)) == 12:
    print((a // 5 - 2) + 4)

else:
    print(-1)