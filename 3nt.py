import math
n,k = [int(i) for i in input().split()]
for i in range(n,k+1,1):
    for j in range(i+1,k+1,1):
        for m in range(j+1,k+1,1):
            if math.gcd(j,m)==1 and math.gcd(i,j)==1 and math.gcd(i,m)==1:
                print("("+str(i)+", "+str(j)+", "+str(m)+")")