for t in range(int(input())):
    n = input()
    i = 0
    check = True
    while i + 1 < len(n) and n[i] < n[i + 1]:
        i += 1
    if i==len(n)-1 or i == 0:
        check = False
    if check == True:
        for j in range(i,len(n)-1,1):
            if ord(n[j+1])>ord(n[j]):
                check = False
                break
    if check:
        print('YES')
    else:
        print('NO')