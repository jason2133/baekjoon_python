a = int(input())
b = 1000 - a
c = 0

if 500 < b :
    c = c + b//500
    b = b - (b // 500) * 500

if 100 <= b and b < 500:
    c = c + b//100
    b = b - (b // 100) * 100

if 50 <= b and b < 100:
    c = c + b//50
    b = b - (b // 50) * 50

if 10 <= b and b < 50:
    c = c + b//10
    b = b - (b // 10) * 10

if 0 < b and b < 10:
    c = c + b

if b == 0:
    c = 0

print(c)
























# a = int(input())
#
# b = 1000 - a
# c = 0
#
# if b // 500 > 0:
#     b = b - (b // 500) * 500
#     c = c + (b // 500)
#
# if b // 100 > 0:
#     b = b - (b // 100) * 100
#     c = c + (b // 100)
#
# if b // 50 > 0:
#     b = b - (b // 50) * 50
#     c = c + (b // 50)
#
# if b // 10 > 0:
#     b = b - (b // 10) * 10
#     c = c + (b // 10)
#
# if b // 5 > 0:
#     b = b - (b // 5) * 5
#     c = c + (b // 5)
#
# if b // 1 > 0:
#     b = b - (b // 1) * 1
#     c = c + (b // 1)
#
# print(c)
#
