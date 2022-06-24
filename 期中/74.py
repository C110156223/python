ans=['red','blue','red','green']

while True:
    guess = input("輸入顏色:")
    guess = guess.split()
    output = str()

    for i in range(4):
        if guess[i] == ans[i]:
            output += '1'
        elif guess[i] in ans:
            output += '2'
        else:
            output += '3'

    if output == "1111":
        print("正確答案")
        break
    else:
        print(output)
        break