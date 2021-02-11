a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    ans = 0
    d = [i for i in range(1, c+1)]
    for j in range(b):
        e = int(input())
        if e in d:
            d.remove(e)
        else:
            ans += 1
    print(ans)
    