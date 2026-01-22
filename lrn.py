l=0
while l!=-1:
    l,r = map(int,input().split())
    n=int(input())
    dem = 0
    for i in range(l,r+1):
        check = 1
        if i<2:
            dem+=1
        else:
            for j in range(2,n+1):
                if i%j==0:
                    check = 0
                    break
        if check:
            dem+=1
    print(dem)
