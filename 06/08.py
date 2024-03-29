unique=set()

num=int(input())

for _ in range(num):
    unique.add(input())

print(num-len(unique))