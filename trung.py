for t in range(int(input())):
    n=int(input())
    a=[]
    cnt=[0]*1000
    maxcnt=0
    for i in range(n):
        a.append(int(input()))
    a.sort()
    for i in range(len(a)):
        cnt[a[i]]+=1
        if cnt[a[i]]>maxcnt:
            maxcnt=cnt[a[i]]
    for i in a:
        if cnt[i]==maxcnt:
            print(i)
            break