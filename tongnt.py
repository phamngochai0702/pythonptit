import math

def snt(s):
    for i in range(2,math.isqrt(s)+1):
        if s%i==0:
            return 0
    return s>1

for t in range(int(input())):
    n = input()
    s = str(n)
    tong = 0
    for i in s:
        tong+=int(i)
    if snt(tong):
        print("YES")
    else:
        print("NO")
