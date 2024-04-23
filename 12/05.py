n=int(input().split('#')[1])
lines=[]

for _ in range(n):
    temp=input().split('#')[0]
    temp.rstrip()
    lines.append(temp)

for line in lines:
    print(line)