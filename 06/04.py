unique=set()


num=int(input())
num+=int(input())

for i in range(num):
    unique.add(input())

both=num-len(unique)
print(num-2*both)