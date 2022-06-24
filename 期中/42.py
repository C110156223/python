a=int(input("輸入a:"))
b=int(input("輸入b:"))
c=int(input("輸入c:"))

b24ac=(b**2)-(4*a*c)
#print(b24ac)
if b24ac<0: #無解
    print(0)

if b24ac>0: #兩相異解
    a1=((-1)*b+b24ac**0.5)/(2*a)
    a2=((-1)*b-b24ac**0.5)/(2*a)
    print(a1)
    print(a2)

if b24ac==int(0): #重根
    a=(-1)*b/(2*a)
    print(a)
