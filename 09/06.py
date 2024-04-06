n=int(input())

inp=list()

for _ in range(n):
    inp.append(int(input()))


for x in range(1, n):
    print(str(inp[x]+inp[x-1]))