s= input()
s1= s.upper()
s2= s.lower()
dem = 0
for i in range(len(s1)):
    if s[i] != s1[i]:
        dem+=1
if dem< len(s1)/2:
    print(s1)
else:
    print(s2)