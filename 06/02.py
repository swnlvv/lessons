n=int(input())

cities=set()

another=0

for i in range(n):
    city=input()
    if city in cities:
        another=1
    else:
        cities.add(city)

if another==0:
    print('OK')
else:
    print('TRY ANOTHER')