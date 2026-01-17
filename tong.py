s = input()
parts = s.split()
a = int(parts[0])
b = int(parts[2])
c = int(parts[4])

if a + b == c:
    print("YES")
else:
    print("NO")