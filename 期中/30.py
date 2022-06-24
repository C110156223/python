'''
que=0
for i in range(10):
    if que>0:
        que=int(input("猜數字(4位數):"))
    elif que=='0000':
        break  
'''    
que=int(input("猜數字(4位數):")) 
ans='1234'
A=0
B=0
for i in range(4):
    if que[i]==ans[i]:
        A+=1
    elif ans[i] in que:
        B+=1
print(A,"A",B,"B")

# right = ['1','2',"3","4"]

# while True:
#     a=0
#     b=0
#     user =list(input('猜四位數字:'))
#     if user.count('0')==4:
#         print('結束')
#         break
#     if len(user)==4:
#         for i in range(4):
#             if (right[i]==user[i]):
#                 a+=1
#             elif(right.count(user[i])==1 and right[i]!=user[i]):
#                 b+=1
#         print(str(a)+'A',str(b)+"B")
#     elif len(user)!=4:
#         print('輸入錯誤')
#     if a==4:
#         break
