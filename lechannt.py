import math

def snt(n):
    if n<=1:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

for t in range(int(input())):
    n=input()
    tong = 0
    check = 1
    for i in range(0,len(n),1):
        tong+=int(n[i])
        if (i%2==0 and int(n[i])%2!=0) or (i%2==1 and int(n[i])%2==0):
            check = 0
            break
    if(snt(tong))==False:
        check = 0
    if check==1:
        print("YES")
    else:
        print("NO")