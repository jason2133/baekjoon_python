a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a// b)
# 사칙연산에서 / 는 나머지 값을 나타내는데, 뒤에 소수점 모조리 나타나고,
# //를 활용하면 뒤에 있는 소수점은 버리고 정수만 답으로 나온다.


print(a%b)