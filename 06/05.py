unique=set()

biling=set()

num=int(input())
num+=int(input())
num+=int(input())

for i in range(num):
    s=input()
    unique.add(s)
    if (s in unique) and (s not in biling):
        biling.add(s)

print(len(biling))