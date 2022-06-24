n=int(input("輸入n:"))
k=int(input("輸入k:"))
kk=int(n//k)
nk=0
if kk>=k:
    nk=kk//k
print("peter可以抽",n+kk+nk,"支紙菸")
