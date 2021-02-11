a = int(input())
hak = []
sco = []
for i in range(a):
    b, c, d = map(str, input().split())
    c = float(c)
    hak.append(c)
    if d == 'A+':
        sc = 4.3
    elif d == 'A0':
        sc = 4.0
    elif d == 'A-':
        sc = 3.7
    elif d == 'B+':
        sc = 3.3
    elif d == 'B0':
        sc = 3.0
    elif d == 'B-':
        sc = 2.7
    elif d == 'C+':
        sc = 2.3
    elif d == 'C0':
        sc = 2.0
    elif d == 'C-':
        sc = 1.7
    elif d == 'D+':
        sc = 1.3
    elif d == 'D0':
        sc = 1.0
    elif d == 'D-':
        sc = 0.7
    elif d == 'F':
        sc = 0.0
    k = c * sc
    sco.append(k)
    
final = sum(sco) / sum(hak)
final += 0.000000000001
print('%.2f' % final)
        
        