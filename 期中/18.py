card=input("").split()

for i in range(5):
    if card[i]=="A":
        card[i]=1
    elif card[i]=="J":
        card[i]=11
    elif card[i]=="Q":
        card[i]=12
    elif card[i]=="K":
        card[i]=13
#print(card)
sum=0
for n in range(5):
    sum+=int(card[n])

print(sum)