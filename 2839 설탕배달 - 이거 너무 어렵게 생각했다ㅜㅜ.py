a = int(input())

# 3kg 혹은 5kg 나누기 해야됨 저 인풋을 말이지

# 15의 배수
if a % 3 == 0 and a % 5 == 0 :
    print(a//5)

elif a == 3 or a == 6 or a == 9 or a == 12 :
    print(a//3)

elif a == 4 or a == 7:
    print("-1")

else:
    # 5의 배수
    if a % 5 == 0 :
        print(a // 5)

    





