cat=False
number=0
s=''

while s!='СТОП':
    s=str(input())
    number+=1
    
    if (('кот' in s) or ('Кот' in s))and not cat:
        
        answer=number
        cat=True
        print(answer)
        break
    

if not cat:
    
    print(-1)