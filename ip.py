for _ in range(int(input())):
    s = input().strip()
    parts = s.split(".")
    if len(parts) != 4:
        print("NO")
        continue

    x, y, z, t = parts

    if not (x.isdigit() and y.isdigit() and z.isdigit() and t.isdigit()):
        print("NO")
        continue

    if int(x) > 255 or int(y) > 255 or int(z) > 255 or int(t) > 255:
        print("NO")
    else:
        print("YES")
