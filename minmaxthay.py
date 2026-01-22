for _ in range(int(input())):
    a, b = input().split()
    m = input()
    n = input()
    min_sum = int(m.replace(a, b)) + int(n.replace(a, b))
    max_sum = int(m.replace(b, a)) + int(n.replace(b, a))
    print(min_sum, max_sum)