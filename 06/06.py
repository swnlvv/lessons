home_num=int(input())
summer_num=int(input())

home=set()

for i in range(home_num):
    home.add(input())

for i in range(summer_num):
    book=input()
    if book in home:
        print('YES')
    else:
        print('NO')