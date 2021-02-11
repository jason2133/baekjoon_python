a = int(input())
b = list(map(int, input().split()))

c = max(b)
d = 0

for i in range(0, a):
    b[i] = b[i] / c * 100

for i in range(0, a):
    d = d + b[i]

print(d / a)











# ex 2
# print(10 / 30 * 100)
# print(20 / 30 * 100)
# print(30 / 30 * 100)

# print((33.33 + 66.66 + 100) / 3)

# print("하하 이제 이해가 되니?")

# ex 3
# print(1 / 100 * 100)
# print(100 / 100 * 100)
# print(100 / 100 * 100)
# print(100 / 100 * 100)

# print((301) / 4)


