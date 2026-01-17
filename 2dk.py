a, k, n = map(int, input().split())
def dk(b):
    if a+b<=n and (a+b)%k==0:
        return True
    else:
        return False
check = False
for b in range(1,n+1):
    if dk(b):
        check = True
        print(b,end=' ')
if check == False:
    print(-1)