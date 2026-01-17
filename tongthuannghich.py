for t in range(int(input())):
    n = input()
    s = str(n)
    tong = 0
    for i in s:
        tong+=int(i)
    if str(tong)==str(tong)[::-1] and len(str(tong))>1:
        print("YES")
    else:
        print("NO")
