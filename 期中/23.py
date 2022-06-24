while True:
    n=int(input("輸入值n(輸入-1可結束):"))
    if n==-1:
        break
    else:
        i=0
        sum=0
        dx=0.001
        while i<=n:
                sum=sum+(i**2)*dx
                i+=dx
        print('%.1f'%sum)
