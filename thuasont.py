for t in range(int(input())):
    n=int(input())
    tam = n
    res = '1'
    for i in range(2,n,1):
        dem = 0
        while tam%i==0:
            dem+=1
            tam//=i
        if dem >0:
            res+=" * " + str(i)+"^"+str(dem)
    print(res)