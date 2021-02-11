a = str(input())

while len(a) > 10:
    print(a[0 : 10], end = '\n')
    a = a[10: ]

if len(a) <= 10:
    print(a)


# a = str(input())
#
# print(len(a))
#
# b = ''
# # 10개 묶어서 프린트하기
# for i in range(1, len(a) // 10 + 1):
#     for j in range(i * 10 - 10, i * 10):
#         if i == 1:
#             b = b + a[j]
#             i = i + 1
#         print(b)
#
# c = ''
# # 마지막에 나머지
# for i in range(((len(a) // 10) * 10), len(a)):
#     c = c + a[i]
#
# print(c)
