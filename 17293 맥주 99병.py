def print1(n):
    if n==1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
    elif n==0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
    else:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")

def print2(n):
    if n==0:
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    elif n==1:
        print("Take one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print(f"Take one down and pass it around, {n} bottles of beer on the wall.")

n=int(input())
nn=n
while nn>-1:
    print1(nn)
    if nn==0:
        if n==1:
            print("Go to the store and buy some more, 1 bottle of beer on the wall.")
        else:
            print(f"Go to the store and buy some more, {n} bottles of beer on the wall.")
    else:
        print2(nn-1)
    nn-=1
    print()