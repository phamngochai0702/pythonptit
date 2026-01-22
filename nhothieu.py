n=int(input())
a=[int(i) for i in input().split()]
a.sort()
used=[0]*1000
check = 0
for i in range(len(a)):
    used[a[i]]+=1
for i in range(1,n+1):
    if used[i]==0:
        print(i)
        check = 1
        break
if check==0:
    print(n+1)