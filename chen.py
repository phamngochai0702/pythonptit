s1=input()
s2=input()
p=int(input())
res=""
if p == 1:
    res=s2+s1
else:
    res=s1[:p-1]+s2+s1[p-1:]
print(res)