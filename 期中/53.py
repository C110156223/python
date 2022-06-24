n=int(input("輸入n值:"))
all={}
for i in range(n):
    name=input("請輸入姓名:")
    mail=input("請輸入電子郵件:")
    all[name]=mail

s=input("輸入要查詢電子郵件的姓名:")
print(s,'的電子郵件為',all[s])
