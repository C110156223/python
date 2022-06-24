n=int(input("輸入n值:"))
nn=round(n/2)
for a in range(nn):
    for b in range(4-a):
        print(" ",end='')
    for b in range(a+1):
        print("*",end='')
    for b in range(a):
        print("*",end='')
    print()
for a in range(nn-2,-1,-1):
    for b in range(nn-a):
        print(" ",end='')
    for b in range(2*a+1):
        print("*",end='')
    print()
