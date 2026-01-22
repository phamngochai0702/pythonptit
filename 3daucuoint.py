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
    if snt(int(n[-3:])) == True and snt(int(n[:3])) ==True:
        print("YES")
    else:
        print("NO")