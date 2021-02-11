# CCW 직선의 방향성 파악 수학적 개념

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

k = x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1

if k > 0: #반직선
    print(1)
    
elif k == 0: #직선
    print(0)
    
elif k < 0: #시계방향
    print(-1)
