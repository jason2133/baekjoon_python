a = str(input())
a1 = a[0:len(a)//2]
a2 = a[len(a)//2:]
left = 0
right = 0

for i in a1:
    left += int(i)

for i in a2:
    right += int(i)

if left == right:
    print('LUCKY')
else:
    print('READY')
    