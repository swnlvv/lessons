line = input().split(sep=': ')
num = int(input())

ans = ''
for word in line:
    length = len(word)
    if length>num:
        if length%num!=0:
            ans+=word.capitalize()+', '
if ans!='':
    ans = ans[:-2]
print(ans)

