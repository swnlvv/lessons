first=set()
second=set()
ffirst=True
while ffirst:
    s=input()
    if s=="":
        ffirst=False
    else:
        first.add(s)

while True:
    s=input()
    if s=="":
        break
    else:
        second.add(s)
    
f_len=len(first)
s_len=len(first)

same=False

if f_len<s_len:
    for x in first:
        if x in second:
            print(x)
            same=True
else:
    for x in second:
        if x in first:
            print(x)
            same=True
    
if not same:
    print('EMPTY')

