import sys
while True:
    n=int(sys.stdin.readline().strip())
    if n==0:break
    max_name,max_score=[""],0
    for i in range(n):
        name,score=input().strip().split()
        if i==0:max_name[0],max_score=name,float(score)
        elif float(score)==max_score:
            max_name.append(name)
        elif float(score)>max_score:
            max_score=float(score)
            max_name=[name]
    print(" ".join(str(e) for e in max_name))