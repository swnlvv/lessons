def spacegame():
    line = input()
    count = 0
    for symbol in line:
        if symbol==" ":
            count+=1
    if count%2==0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")

spacegame()