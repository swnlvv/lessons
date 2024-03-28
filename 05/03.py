cat=False
number=0
s=''

while s!='СТОП':
    s=str(input())
    number+=1
    
    if (('кот' in s) or ('Кот' in s))and not cat:
        
        answer=number
        cat=True
    

if cat:
    print(answer)
else:
    print(-1)
