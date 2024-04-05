s=input()
ans=True

for x in s:
    letterrange=False
    if ord('a')<=ord(x)<=ord('z'):
        letterrange=True
    elif ord('0')<=ord(x)<=ord('9'):
        letterrange=True
    elif x=="_":
        letterrange=True
    
    if not letterrange:
        print('Неверный символ:', x)
        ans=False
        break
    

if ans:
    print('OK')