list=[]
while True:
    do=str(input("輸入代辦事項(輸入end可結束):"))
    list.append(do)
    if do=="end":
        n=len(list)
        for i in range(1,n):
            print(i,'.',list[i-1])
        break