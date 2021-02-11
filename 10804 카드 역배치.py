a = [i for i in range(1, 21)]
for i in range(10):
    b, c = map(int, input().split())
    d = a[b-1:c]
    a[b-1:c] = d[::-1]

for i in a:
    print(i, end = ' ')
