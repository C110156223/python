km=float(input("輸入路程公里數(km):"))
m=km*1000
money=75
if m>1500:
    over=(m-1500)//250
    money+=over*5
    if (m-1500)%250>0:
        money+=5
    print("所需車資為:",int(money))
else:
    print("所需車資為:",int(money))

