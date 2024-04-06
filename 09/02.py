
n=int(input())

lines=list()

for _ in range(n):
    lines.append(input())

search=input()
for item in lines:
    if search in item:
        print(item)