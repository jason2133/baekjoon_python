alpha = 'abcdefghijklmnopqrstuvwxyz'
a = int(input())
for i in range(1, a+1):
    b = []
    c = input()
    c = c.lower()
    for j in alpha:
        d = c.count(j)
        b.append(d)

    if min(b) == 0:
        print('Case %s: Not a pangram' % (i))
    elif min(b) == 1:
        print('Case %s: Pangram!' % (i))
    elif min(b) == 2:
        print('Case %s: Double pangram!!' % (i))
    elif 3 <= min(b):
        print('Case %s: Triple pangram!!!' % (i))
    
