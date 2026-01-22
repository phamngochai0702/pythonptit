for t in range(int(input())):
    s=input()
    tong = 0
    res1=''
    for i in s:
        if not i.isdigit():
            res1+=i
        else:
            tong+=int(i)
    res1=''.join(sorted(res1))+str(tong)
    print(res1)


