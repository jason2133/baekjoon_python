i = 1
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0): break
    print('Triangle #{}'.format(i)); i += 1
    if (a== -1): print('Impossible.' if c**2-b**2<=0 else 'a = {:.3f}'.format((c**2-b**2)**0.5))
    elif (b== -1): print('Impossible.' if c**2-a**2<=0 else 'b = {:.3f}'.format((c**2-a**2)**0.5))
    else: print('c = {:.3f}'.format((a**2+b**2)**0.5)) 
    print()