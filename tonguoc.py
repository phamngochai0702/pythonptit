import math
tong = 0
for t in range(int(input())):
    n= int(input())
    i=2
    while i*i<=n:
        while n%i==0:
            tong+=i
            n=n//i
        i+=1
    if n>1:
        tong+=n
print(tong)