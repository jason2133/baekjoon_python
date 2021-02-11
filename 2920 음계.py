a = list(map(int, input().split())) # 인풋 받기

b = sorted(a) # 오름차순

c = sorted(a, reverse=True) # 내림차순


if a == b:
    print("ascending")

elif a == c:
    print("descending")

else :
    print("mixed")











