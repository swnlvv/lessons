s = input()
a=s.split(' ')
s1=''
for i in range(len(a)):
    if (i+1)%3==0:
        s1=s1+a[i]+' '
        
s1=s1.rstrip()
print(s1)