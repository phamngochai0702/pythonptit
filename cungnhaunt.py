import math
n,k = [int(i) for i in input().split()]
dem = 0
for i in range(10**(k-1),10**(k),1):
    if math.gcd(n,i)==1:
        dem+=1
        if dem %10==0:
            print(i)
        else:
            print(i,end=' ')