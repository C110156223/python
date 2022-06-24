x=float(input("輸入x座標點:"))
y=float(input("輸入y座標點:"))
d=int(x**2+y**2)
if x>0 and y>0:
    print("該點位於第一象限,離原點距離為根號",d)
elif x>0 and y<0:
    print("該點位於第四象限,離原點距離為根號",d)
elif x<0 and y>0:
    print("該點位於第二象限,離原點距離為根號",d)
elif x<0 and y<0:
    print("該點位於第三象限,離原點距離為根號",d)
elif x==0 and y==0:
    print("該點位於原點")
elif x==0 and y>0:
    print("該點位於上半Y軸上,離原點距離為根號",d)
elif x==0 and y<0:
    print("該點位於下半Y軸上,離原點距離為根號",d)
elif x>0 and y==0:
    print("該點位於右半X軸上,離原點距離為根號",d)
elif x<0 and y==0:
    print("該點位於左半X軸上,離原點距離為根號",d)
