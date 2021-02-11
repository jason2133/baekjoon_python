import sys
t=int(sys.stdin.readline().strip())
for i in range(t):
    print("Scenario #{}:".format(i+1))
    m=int(sys.stdin.readline().strip())
    voca=[]
    for _ in range(m):
        voca.append(sys.stdin.readline().strip())
    n=int(sys.stdin.readline().strip())
    for _ in range(n):
        pwd=list(map(int,sys.stdin.readline().strip().split()))
        for e in pwd[1:]:
            print(voca[e],end="")
        print()
    if i!=t-1:print()