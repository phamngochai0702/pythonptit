import math
n = int(input())
kq=0
for j in range(36,n):
    dem = 0
    for i in range(1,math.isqrt(j)+1):
        if j%i == 0:
            if i*i==j:
                dem += 1
            else:
                dem+=2
            if dem>9:
                break
    if dem ==9:
        kq+=1
print(kq)
