def check(n):
    s = str(n)
    for i in s:
        if int(i)%2==1:
            return False
    if  len(s)%2==1:
        return False
    if s!=s[::-1]:
        return False
    return True
for t in range (int(input())):
    n = int(input())
    for i in range(22,n+1):
        if check(i):
            print(i,end = ' ')
    print()
