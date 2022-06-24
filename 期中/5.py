M=int(input("請輸入M值:"))
total=i=1
while total<=M:
    total *= i
    i+=1
print("超過M為",M,"的最小階層N值為:",i-1)