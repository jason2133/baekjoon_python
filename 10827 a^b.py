from decimal import Decimal, getcontext

def main():
    r, n = input().split(' ')
    getcontext().prec = 1101
    print("{0:f}".format(Decimal(r) ** int(n)))

if __name__ == '__main__':
    main()