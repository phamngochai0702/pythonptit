for t in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    check = 0
    used=[0]*1000
    for i in range(len(a)):
        used[a[i]]+=1
    for i in range(a[0],a[-1]+1):
        if used[i]>n/2:
            print(i)
            check = 1
    if check==0:
        print("NO")