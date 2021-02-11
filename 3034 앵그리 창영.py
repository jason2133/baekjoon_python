a, b, c = map(int, input().split())
for i in range(a):
    d = int(input())
    # 대각선 길이
    e = (b**2 + c**2)**0.5
    if d <= e:
        print('DA')
    else:
        print('NE')
    
    