cat=False
number=0
s=''
count=0
answer=-1
while s!='СТОП':
    s=str(input())
    number+=1
    words=s.split()
    l=len(words)
    for i in range(l):
        if ('кот' in words[i]) or ('Кот' in words[i]):
            count+=1
            if not cat:
        
                answer=number
                cat=True
    
print(count, answer)
        
    

