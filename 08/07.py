output=str()
n=int(input())

for i in range(n):
    s=input()
    if ('кот' in s):
        output=output+str(i+1)+' '+str(s.find('кот')+1)+'\n'

output=output.rstrip('\n')
print(output)