dp = [0 for i in range(10005)]
dp[1] = 1
dp[2] = 1
for i in range(3, 10005):
    dp[i] = dp[i-1] + dp[i-2]
    
a = int(input())
for i in range(1, a+1):
    b, c = map(int, input().split())
    d = dp[b] % c
    print('Case #%s: %s' % (i, d))
    

