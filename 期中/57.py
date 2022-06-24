meal,combo=input("請選擇主餐及升級的套餐(用空格分開):").split()
drink=input("是否升級成大杯飲料:")
fries=input("是否升級成大薯:")

if meal=="1":
    money=72
    if combo=="A":
        money+=55
    elif combo=="B":
        money+=68
elif meal=="2":
    money=62
    if combo=="A":
        money+=55
    elif combo=="B":
        money+=68
elif meal=="3":
    money=82
    if combo=="A":
        money+=55
    elif combo=="B":
        money+=68
elif meal=="4":
    money=44
    if combo=="A":
        money+=55
    elif combo=="B":
        money+=68
elif meal=="5":
    money=60
    if combo=="A":
        money+=55
    elif combo=="B":
        money+=68

if drink=="是":
    money+=7

if fries=="是":
    money+=13

print("總共為",money,"元")