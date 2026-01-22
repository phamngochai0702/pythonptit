S="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM._"
s= input()
check = 1
if len(s)<3:
    check = 0
for i in s:
    if not(i in S):
        check = 0
        break
if s[-3:] != ".py":
    check = 0
if not(check):
    print("no")
else:
    print("yes")