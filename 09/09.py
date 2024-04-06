n=int(input())

start=[]

for _ in range(n):
    start.append(input())

for x in range(n):
    print(start[x])

print()

for x in range(n):
    print(str(int(start[x])*3))