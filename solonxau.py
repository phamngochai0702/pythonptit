for t in range(int(input())):
    s = input()
    res = ''
    maxx = 0

    for i in s:
        if i.isdigit():
            res += i
        else:
            if res != '':
                maxx = max(maxx, int(res))
                res = ''

    if res != '':
        maxx = max(maxx, int(res))

    print(maxx)