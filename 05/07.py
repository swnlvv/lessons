war='Евразия'
peace='Остазия'

question_war='С кем война?'
question_peace='С кем мир?'
change='Меняем'

n=int(input())

for i in range(n):
    question=input()
    if question==question_war:
            print(war)
    elif question==question_peace:
            print(peace)
    else:
           war, peace = peace, war