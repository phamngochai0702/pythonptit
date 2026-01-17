for t in range(int(input())):
    n = input()
    s = str(n)
    tong = 0
    for i in s:
        tong+=int(i)
    if tong%3==0:
        print("YES")
    else:
        print("NO")
