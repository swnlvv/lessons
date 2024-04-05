n=int(input())

while n<=1000000:
    s=str(n)[0]
    n*=int(s)
    if int(s)==1:
        break

print(n)