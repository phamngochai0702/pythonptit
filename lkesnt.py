from math import isqrt
def snt(a):
    if a<2:
        return 0
    else:
        for i in range(2,isqrt(a)+1,1):
            if a%i==0:
                return 0
    return 1
n=int(input())
a=[int(i) for i in input().split()]
used=[0]*999999
j = [0]*999999
k=0
for i in range(0,n):
    if snt(a[i])==1:
        used[a[i]]+=1
        j[k]=a[i]
        k+=1
for i in range(0,k):
    if used[j[i]]!=0:
        print(j[i],used[j[i]],sep=" ")
        used[j[i]]=0
