def solve(A, B):
    if(B % 2 > 0):
        return solve(A, B - 1) * A
    elif(B == 0):
        return 1
    elif(B == 1):
        return A
    else:
        result = solve(A, B//2)
        return result ** 2 % p

N, K = map(int, input().split())    

n_part = 1
nk_part = 1

p =  1000000007

for num in range(1, N+1):
    n_part *= num; n_part %= p

for num in range(1, K+1):
    nk_part *= num; nk_part %= p

for num in range(1, N-K+1):
    nk_part *= num; nk_part %= p
    
nk_part = solve(nk_part, p-2) % p

result = (n_part * nk_part) % p
print(result)