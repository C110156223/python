a=input("輸入A的朋友:").split()
b=input("輸入B的朋友:").split()
count=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            count+=1
print(count)