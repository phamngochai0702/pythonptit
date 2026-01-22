s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for t in range(int(input())):
    n,k = map(int,input().split())
    res=''
    for i in range(n):
        res = res + s[i] + res
    print(res[k-1])