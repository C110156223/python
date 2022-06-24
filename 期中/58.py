num=[]
for i in range(1,11):
    a=int(input("輸入第{0}個數字:".format(i)))
    num.append(a)
num.sort()
print("最大的三個數字為:",num[9],num[8],num[7])
print("最小的三個數字為:",num[2],num[1],num[0])