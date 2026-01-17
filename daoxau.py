for t in range(int(input())):
    s=input()
    s1=s[::-1]
    check = True
    for j in range(len(s1)-1):
        if abs(ord(s[j])-ord(s[j+1])) != abs(ord(s1[j])-ord(s1[j+1])):
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')