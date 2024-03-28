n=int(input())
ans=0
for i in range(0, n):
    if i%2!=0:
        ans-=int(input())
    else:
        ans+=int(input())
print(ans)