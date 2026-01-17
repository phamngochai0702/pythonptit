def check(n):
    s = str(n)
    if sum(int(i) for i in s) %10 != 0:
        return False
    for i in range(len(s)-1):
            if(abs(ord(s[i])-ord(s[i+1])) !=2):
                return False
    return True


for t in range(int(input())):
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')
