que=list(input("猜數字(4位數):")) 
ans=[1,2,3,4]
A=0
B=0
for i in range(4):
    if que[i]==ans[i]:
        A+=1
    elif ans[i] in que:
        B+=1
print(A,"A",B,"B")
