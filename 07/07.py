s=input()
n=len(input)

ans=''
for i in range(n):
    ans+=ord(s[i])+', '

ans=ans[:-2]