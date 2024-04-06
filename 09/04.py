n = int(input())

lines=list()

for _ in range(n):
    lines.append(input())

n=int(input())

ans=list()
7
for _ in range(n):
    x=int(input())
    ans.append(lines[x-1])

for x in range(n):
    print(ans[x])