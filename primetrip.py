from math import isqrt
def prime(n):
    if n <2:
        return False
    else:
        for i in range(2, isqrt(n)+1,1):
            if n % i == 0:
                return False
    return True

for case in range(int(input())):
    cnt = 0
    for i in range(int(input())-5):
        if prime(i) and prime(i+6):
            if prime(i+2) or prime(i+4):
                cnt += 1
    print(cnt)