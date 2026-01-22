a = []
while len(a) < 10:
    a.extend(map(int, input().split()))
cnt=0
used=[0]*(10**5)
for i in range(10):
    if used[a[i]%42]==0:
        cnt+=1
        used[a[i]%42]=1
print(cnt)