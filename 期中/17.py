c1=input("")
c11,c12=input("").split()
c21,c22=input("").split()
a1=input("")
a11,a12=input("").split()
a21,a22=input("").split()
if c1==a1:
    new11=int(c11)+int(a11)
    new12=int(c12)+int(a12)
    new21=int(c21)+int(a21)
    new22=int(c22)+int(a22)
    print(new11,new12)
    print(new21,new22)
else:
    print("兩個矩陣無法相加")

