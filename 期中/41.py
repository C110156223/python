T=int(input("搭了幾次電梯:"))
floor=[1]
for i in range(T):
    a=input("")
    floor.append(int(a))

money=0

if floor[1]<=1:
    print("請選擇其他樓層")
else:
    f=int(floor[1])-1
    money+=20*f

if floor[2]>floor[1]:
    f=floor[2]-floor[1]
    money+=20*f
elif floor[2]<floor[1]:
    f=floor[1]-floor[2]
    money+=10*f

if floor[3]>floor[2]:
    f=floor[3]-floor[2]
    money+=20*f
elif floor[3]<floor[2]:
    f=floor[2]-floor[3]
    money+=10*f

if floor[4]>floor[3]:
    f=floor[4]-floor[3]
    money+=20*f
elif floor[4]<floor[3]:
    f=floor[3]-floor[4]
    money+=10*f

if floor[5]>floor[4]:
    f=floor[5]-floor[4]
    money+=20*f
elif floor[5]<floor[4]:
    f=floor[4]-floor[5]
    money+=10*f

print(money,"元")