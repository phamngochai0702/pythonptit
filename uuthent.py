import math

def snt(n):
    if n<=1:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
for t in range(int(input())):
    s=input()
    nt=0
    knt=0
    for i in s:
        if i!='2' and i!='3' and i!='5' and i!='7':
            knt+=1
        else:
            nt+=1
    if nt<knt or snt(len(s))==False:
        print('NO')
    else:
        print('YES')
