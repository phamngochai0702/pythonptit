t=int(input())
while t != 0:
    ok = 1
    s = input()
    for i in range(len(s)):
        if s[i]!="4" and s[i]!="7":
            ok = 0
    if ok == 1:
        print("YES")
    else:
        print("NO")
    t= t-1