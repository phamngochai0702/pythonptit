import math
def snt(x):
    if x<2:
        return False
    for i in range(2,math.isqrt(x)+1):
        if x%i==0:
            return False
    return True

for t in range(int(input())):
    n = input()
    check = 1
    for i in range(0,len(n)):
        if snt(int(n[i]))==False and snt(i)== True:
            check = 0
        if(snt(int(n[i]))==True and snt(i)== False):
            check = 0
    if check==1:
        print("YES")
    else:
        print("NO")