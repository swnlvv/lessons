n = int(input())

soldiers=[]

for _ in range(n):
    soldiers.append(input())

retribution=int(input())
reps=int(input())

for _ in range(reps):
    del soldiers[retribution-1::retribution]

for i in soldiers:
    print(i)