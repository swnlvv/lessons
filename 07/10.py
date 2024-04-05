n=int(input())
s1=''
s=input()
##работает только для натуральных n!!!!
for x in s:
    if (ord('А')<=ord(x)<=ord('Я')):
        if ord(x)+n>ord('Я'):
            x=chr(ord(x)-32)
        s1+=chr(ord(x)+n)
    elif (ord('а')<=ord(x)<=ord('я')):
        if ord(x)+n>ord('я'):
            x=chr(ord(x)-32)
        s1+=chr(ord(x)+n)
    else:
        s1+=x

print(s1)