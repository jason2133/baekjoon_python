while True:
    a = float(input())
    if a == -1.0:
        break
    else:
        b = a * 0.167
        print('Objects weighing %.2f on Earth will weigh %.2f on the moon.' % (a, b))
    
    