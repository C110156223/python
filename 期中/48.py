n=int(input("輸入筆數:"))
t={}
for i in range(n):
    eng,chn=input("").split()
    t[eng]=chn
#print(t)
s=input("輸入欲查詢單字:")
print(s,'中文意思為',t[s])
