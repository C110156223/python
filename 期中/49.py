a=input("輸入英文句子:").split()
rev=[]
for i in range(len(a)):
    r=a.pop(len(a)-1)
    rev.append(r)
print("輸出結果:",rev)