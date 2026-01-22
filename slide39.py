X = float(input())0
lai_thang = 0.006
for i in range(3):
    X = X * (1 + lai_thang) ** 6
print(round(X, 2))