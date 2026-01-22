res=input()
tong = 100
dem=0
while tong>9:
    dem+=1
    tong = 0
    for i in res:
        tong+=ord(i)-48
    res=str(tong)
print(dem)