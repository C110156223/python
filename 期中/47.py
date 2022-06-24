n=int(input("輸入比數n:"))
a=int(input("金牌數量:"))
b=int(input("銀牌數量:"))
c=int(input("銅牌數量:"))
d=int(input("優牌數量:"))
if a>n:
    a=n
if b>n:
    b=n
if c>n:
    c=n
if d>n:
    d=n
list1=[a,b,c,d]
list2=['金牌','銀牌','銅牌','優牌']
print(list2[0],"得到",list1[0],"面")
print(list2[1],"得到",list1[1],"面")
print(list2[2],"得到",list1[2],"面")
print(list2[3],"得到",list1[3],"面")
