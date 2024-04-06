n=int(input())

lines=list()

for _ in range(n):
    lines.append(input())

number=int(input())
ans=''

for item in lines:
    ans=ans+item[number-1]

print(ans)