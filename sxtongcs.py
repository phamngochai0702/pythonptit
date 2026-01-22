for t in range(int(input())):
    n = int(input())
    a = input().split()
    b = []
    for s in a:
        tong = 0
        for ch in s:
            tong += int(ch)
        b.append((tong, int(s), s))
    b.sort()
    for x in b:
        print(x[2], end=' ')
    print()