a=input("string_a:")
b=input("string_b:")
s=[]
for i in a:
    for j in b:
        if i==j:
            s.append(i)

s.sort()        
print(s)