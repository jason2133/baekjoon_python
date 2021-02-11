a = int(input())

for i in range(a):
    b = input().split()
    c = input()
    sound = []
    ans = []
    
    while c != 'what does the fox say?':
        c = c.split(' goes ')
        sound.append(c[1])
        c = input()
       
    for j in b:
        if j not in sound:
            ans.append(j)
           
    print(' '.join(ans))
    
