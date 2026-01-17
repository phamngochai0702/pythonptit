s=input()
res= ''
dem = 0
for i in range(len(s)-1,-1,-1):
    res+=s[i]
    dem+=1
    if dem == 3:
        res+=','
        dem = 0
res= res[::-1]
if res[0]==',':
    res=res[1:]
print(res)