print("Вы любите котиков? да/нет")

cats=str(input())

print("Вы умеете программировать? да/нет")

it=str(input())

if ((cats!="да") and (cats!="нет"))or((it!="да") and (it!="нет")):
    print("Неверный ответ")

    pass

if (cats=="да")and (it=="да"):

    print("Замечательно, и мы!")


if (cats=="нет")and (it=="да"):

    print("Полюбите котиков!!!")

if (cats=="да")and (it=="нет"):

    print("А коты умеют")

if (cats=="нет")and (it=="нет"):

    print("Вы незаурядный человек")