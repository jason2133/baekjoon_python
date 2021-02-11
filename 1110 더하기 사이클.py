a = int(input())
c = 0

if a < 10:
    b = str('0') + str(a)
else :
    b = str(a)

c = int(b[0]) + int(b[1])
d = b[1] + str(c)


