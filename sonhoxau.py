for t in range(int(input())):
    s = input()
    res = ''
    minn = 10**20

    for i in s:
        if i.isdigit():
            res += i
        else:
            if res != '':
                minn = min(minn, int(res))
                res = ''

    if res != '':
        minn = min(minn, int(res))

    print(minn)