eng=input("輸入一串小寫英文:")

for i in eng:
    if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
        eng=eng.replace(i,'.')
    
print(eng)