n=int(input())

output=str()

for _ in range(n):
    s=input()
    if s[0:2]=="%%":
        output=output+s[2:]+'\n'
    elif s[0:4]=="####":
        pass
    else:
        output=output+s+'\n'

output=output.rstrip('\n')
print(output)