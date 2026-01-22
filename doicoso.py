for t in range(int(input())):
    n,i=map(int,input().split())
    if i ==2:
        print(bin(n)[2:])
    if i==8:
        print(oct(n)[2:])
    if i == 16:
        print((hex(n)[2:]).upper())
