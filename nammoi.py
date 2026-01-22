n = int(input())
res = []
for _ in range(n):
    s = input()
    if s not in res:
        res.append(s)
print(len(res))
