a = int(input())
for i in range(a):
    b, c = map(str, input().split())
    c = int(c)
    d = 'A'
    if c in range(97, 101):
        d = 'A+'
    elif c in range(90, 97):
        d = 'A'
    elif c in range(87, 90):
        d = 'B+'    
    elif c in range(80, 87):
        d = 'B'    
    elif c in range(77, 80):
        d = 'C+'
    elif c in range(70, 77):
        d = 'C'        
    elif c in range(67, 70):
        d = 'D+'        
    elif c in range(60, 67):
        d = 'D'        
    elif c in range(0, 60):
        d = 'F'    
       
    print('%s %s' % (b, d))
        
        
        
        