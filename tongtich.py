for t in range(int(input())):
    n = input()
    tong=0
    tich=1
    check = 0
    for i in range(0,len(n)):
        if i%2==0:
            tong+=int(n[i])
        else:
            if int(n[i])!=0:
                tich*=int(n[i])
                check = 1
    if check ==0:
        tich=0
    print(tong,tich)