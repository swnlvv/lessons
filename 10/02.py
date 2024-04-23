n=int(input())

students=[]

for _ in range(n):
    students.append(input())

for i in students:
    print(i)

print()

for i in students:
    if ('4' in i) or ('5' in i):
        print(i) 
