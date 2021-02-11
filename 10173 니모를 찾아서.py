while True:
    a = input()
    if a == 'EOI':
        break
    a = a.lower()
    if 'nemo' in a:
        print('Found')
    else:
        print('Missing')
    
    