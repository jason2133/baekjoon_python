c = []
while True:
    try:
        if len(c)>=0 and len(c)<=100:
            a = input()
            a.strip()
            if len(a) > 0 and len(a) <= 100:
                c.append(a)

            else: break

    except EOFError: break

for n in c:
    print(n)