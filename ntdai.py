import math

def snt(n):
    if n <=1:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

for t in range(int(input())):
    n = input()
    s=n[::-1]
    res =''
    if(len(n))<=4:
        if snt(int(n)):
            print('YES')
        else:
            print('NO')
            break
    else :
        for i in range(0,4,1):
            res+=s[i]
        s=res[::-1]
        if snt(int(s)):
            print('YES')
        else:
            print('NO')


