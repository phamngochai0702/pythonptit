n=int(input())
a=[float(i) for i in input().split()]
a.sort()
tong=0
vitril = 0
vitrir = n-1
for i in range(1,n):
    if a[i]==a[0]:
        vitril=i
for j in range(n-2,vitril,-1):
    if a[j]==a[n-1]:
        vitrir=j
for i in range(vitril+1,vitrir):
    tong+=a[i]
kq=tong/(vitrir-vitril-1)
print(format(kq,'.2f'))