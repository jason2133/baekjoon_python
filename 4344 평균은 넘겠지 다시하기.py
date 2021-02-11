a = int(input())

b = [[int(x) for x in input().split()] for y in range(a)]

print(b)
c = 0

for i in range(1, b[0][0] + 1):
    c = c + b[0][i]

print(c)

# 3
# 3 1 2 3
# 4 1 2 3 4
# 5 1 2 3 4 5

# for i in range(int(a)):
#     for j in range(1, b[i][0] + 1):
#         c = c + b[i][j]
#
# print(c) 이건 모든 원소를 다 더해버렸네



# # 2차원 리스트를 적용해야 되나?
#
# a = int(input())
# b = []
#
# for i in range(int(a)):
#     for j in i:
#         b = a.append[i][j]
#
# print(b)



