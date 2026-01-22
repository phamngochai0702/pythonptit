for t in range(int(input())):
    n = int(input())
    a = input().split()
    b = []
    for s in a:
        tich=1
        for ch in s:
            tich *= int(ch)
        b.append((tich, int(s), s))
    b.sort()
    for x in b:
        print(x[2], end=' ')
    print()