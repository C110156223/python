while(True):
    code = input("檢測的字串(end結束):")
    path = int()

    if code == "end":
        break
    else:
        char = input("檢測的單一字元:")
        for i, alpha in enumerate(code):
            if alpha == char:
                path += 1

        print(f"字元{char}出現次數為:{path}")
        break
