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
dict={"金牌":a,"銀牌":b,"銅牌":c,"優牌":d}
for g,m in dict.items():
    print(g,"得到",m,"面")
