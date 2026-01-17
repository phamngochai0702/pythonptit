for t in range(int(input())):
    n = input()
    check = True
    for i in range(len(n)):
        if n[i]!='1' and n[i]!='2' and n[i]!='0':
            check = False
    if check:
        print('YES')
    else:
        print('NO')