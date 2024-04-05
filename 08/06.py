length=int(input())

n=int(input())

output=str()

for i in range(n):
    s=input()
    if len(s)>length:
        output=output+s[0:length-3]+'...'+'\n'
    else:
        output=output+s+'\n'
output=output.rstrip("\n")
print(output)