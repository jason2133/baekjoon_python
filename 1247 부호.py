for i in range(3):
    a = int(input())
    b = []
    for j in range(a):
        c = int(input())
        b.append(c)
    
    if sum(b) == 0:
        print('0')
    elif sum(b) > 0:
        print('+')
    else:
        print('-')
    
    