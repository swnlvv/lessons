count=0
n=-1
sum=0
while n!=0:
    n=int(input())
    sum+=n
    
    count+=1
    if sum==10:
        print(count)
        break