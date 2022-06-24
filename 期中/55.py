A=['飢餓遊戲3','解憂雜貨店','怪獸與他們的產地','哈利波特6','我的阿富汗筆友','祈念之樹','樓下的房客','小王子']
B=['房思琪的初戀樂園','等一個人咖啡','鬼滅之刃14','神農嘗百草','麥田捕手','老人與海','傲慢與偏見','與神同行']

find=input("輸入欲租借的書籍:")
if find in A:
    for i in range(len(A)):
        if find == A[i]:
            num=i+1
    print("在書架A的第",num,"本")

elif find in B:
    for i in range(len(B)):
        if find == B[i]:
            num=i+1
    print("在書架B的第",num,"本")
    
else:
    print("查無此書籍")