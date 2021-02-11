for i in range(1, 101):
    for a in range(2, i):
        for b in range(a, i):
            for c in range(b, i):
                if i**3 == (a**3) + (b**3) + (c**3):
                    print('Cube = %s, Triple = (%s,%s,%s)' % (i, a, b, c))


