chn=int(input("輸入國文分數:"))
eng=int(input("輸入英文分數:"))
math=int(input("輸入數學分數:"))
pe=int(input("輸入體育分數:"))
com=int(input("輸入程式設計分數:"))
avg=(chn+eng+math+pe+com)/5
print("平均分數:%.2f"%avg)
score=[chn,eng,math,pe,com]
max=max(score)
min=min(score)
#sub={'國文':chn,'英文':eng,'數學':math,'體育':pe,'程式設計':com}
print("最高分科目為",max)
print("最低分科目為",min)
