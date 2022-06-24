num=int(input("輸入金額:"))
count=0

while(True):
    if num>=100:
        num-=100
        count+=1
    else:
        if num>=50:
            num-=50
            count+=1
        else:
            if num>=10:
                num-=10
                count+=1
            else:
                if num>=5:
                    num-=5
                    count+=1
                else:
                    if num>=1:
                        num-=1
                        count+=1
                    else:
                        if num<=0:
                            break
print(count)
