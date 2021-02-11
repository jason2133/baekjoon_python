a = int(input())
b = a % 14

if b == 1:
    print('baby')
elif b == 2:
    print('sukhwan')
elif b == 5:
    print('very')
elif b == 6:
    print('cute')
elif b == 9:
    print('in')
elif b == 10:
    print('bed')
elif b == 13:
    print('baby')
elif b == 0:
    print('sukhwan')
   
elif b == 3 or b == 7 or b == 11:
    if a // 14 < 3:
        print('tururu' + 'ru'*(a//14))
    else:
        print('tu+ru*%s' % (a//14 + 2))
        
else:
    if a // 14 < 4:
        print('turu' + 'ru'*(a//14))
    else:
        print('tu+ru*%s' % (a//14 + 1))        
    
    