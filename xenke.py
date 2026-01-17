for t in range(int(input())):
    s = input()
    check = 1
    for i in range(2,len(s),2):
        if s[0]!=s[i]:
            check = 0
    if s[0]==s[1] or len(s)%2==0:
        check = 0
    if check==1:
        print("YES")
    else:
        print("NO")

