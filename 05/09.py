n=int(input())

s=''
count=0

for _ in range(n):
    s=str(input())
    words=s.split()
    l=len(words)
    for i in range(l):
        if ('кот' in words[i]) or ('Кот' in words[i]):
            count+=1
        if (('пёс' in words[i]) or ('Пёс' in words[i])) and count>0:
            count-=1
    
if count>0:
    print('МЯУ')
else:
    print('НЕТ')
      