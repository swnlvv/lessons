n=int(input())

cats=[]
ans=[]
 
count=0
for i in range(n):
    line=input()
    count+=1
    if 'кот' in line:
        ans.append(str(count)+' '+(str(line.find('кот')+1)))
    
for cat in ans:
    print(cat)