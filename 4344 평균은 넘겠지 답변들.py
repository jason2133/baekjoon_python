# 한결이형
a = int(input())
b =[]
for i in range(0,a):
    c=input().split()
    b.append(c)

for j in b:
    j = list(map(int, j))
    n = 0
    for k in range(1,j[0]+1):
        n = n + j[k]
    average = n / j[0]
    m= 0
    for k in range(1,j[0]+1):
        if j[k] > average:
            m = m + 1
    print('%0.3f%%'%(round(m/j[0], 5)*100))

# 상우형
c = int(input())
for i in range(c):
    arr = [int(a) for a in input().split()[1:]]
    sum = 0
    for j in arr:
        sum += j
    avg = sum / len(arr)
    overAvgCount = 0
    for j in arr:
        if j > avg: overAvgCount += 1
        else: pass
    print("%.3f%%" % (overAvgCount / len(arr) * 100))

# 지원이
test_t = int(input())
arr=list()
for i in range(0, test_t):
    scores = list(input().rstrip().split(" "))
    test_l = int(scores[0])
    count = 0
    for k in range(0, test_l+1):
        scores[k]=int(scores[k])
    average = (sum(scores) - test_l)/float(test_l)
    for k in range(1, test_l+1):
        if scores[k] > average:
            count = count + 1
    arr.append((count/test_l)*100)
    scores.clear()

for i in range(0, test_t):
    print("%.3f%%" % arr[i])





