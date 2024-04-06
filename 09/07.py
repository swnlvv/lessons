
n=int(input())

lines=list()

for _ in range(n):
    lines.append(input())


search=list()

l=int(input())

for _ in range(l):
    search.append(input())

for item in lines:
    output=True
    for word in search:
        if word not in item:
            output=False
    if output:
        print(item)