SS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    str=input()
    if str=='0':
        break
    n,s = str.split()
    n = int(n)
    res = ''
    for i in s:
        i = SS[(SS.find(i)+n)%28]
        res+=i
    print(res[::-1])
