# count 함수를 쓰면 되는구나!

a = int(input())
b = int(input())
c = int(input())

k = str(a * b * c)

for i in range(10):
	print(k.count(str(i)))

