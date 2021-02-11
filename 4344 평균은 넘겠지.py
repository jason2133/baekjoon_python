a = int(input())

c = 0
e = 0

for i in range(0, int(a)):
    b = list(map(int, input().split())) # list로 받아들이는 것도 하나의 방법이구나!
    for j in range(1, len(b)):
        c = c + b[j] # 개수가 아닌 전체 원소의 합
        d = c // b[0] # 평균
    print(d)
    # for k in range(1, len(b)):
    #     if b[k] > d:
    #         e = e + 1
    #     else :
    #         e = e



    # b = sys.stdin.readline().split() #readline, 즉 줄을 읽어라!

    # print(int(b[1]) + int(b[2]) + int(b[3]))

# for i in range(1, len(b)):
#     c = int(b[i]) + c #맨앞값을 제외한 나머지 값 더하기
#     print(c)
        # d = c // int(b[0])  # 평균 구하기
        # if int(b[i]) > d:
        #     e = e + 1
        #     f = e / int(b[0])
        #     print(f)



































# # 다시해봐야되는데이거;
# k = int(input()) # 전체 경우의 수 제시
#
# a = int(input())  # 전체 사람 명수
# b = list(map(int, input().split())) # 점수 리스트
#
# c = 0
#
# for i in range(0, a):
#     c = c + b[i] # 모든 점수의 합
#
# d = c / a  # 평균
#
# e = 0
#
# for i in range(0, a):
#     if b[i] > d:
#         e = e + 1  # 평균 넘는 사람들 인원수
#
# print(round((e / a * 100), 3), end = '%')
#
#
#




