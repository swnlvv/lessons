first=input()
output=False

while  '  ' in first:
    first.replace('  ', ' ')

first.split()

n=int(first[0])
sum_inp=int(first[2])

ans=""
total=0
for _ in range(n):

    line=input()
    while " " in line:
        line.replace(' ', '')

    line.rsplit('*')
    price=int(line[0])
    others=line[1]
    others.rsplit("=")
    amount=int(others[0])
    check=int(others[1])

    true_check=amount*price
    total+=true_check
    
    if check!=true_check:
        output=True
        ans+=' '+str(n+1)

if ans=='':
    print('0')
else:
    diff=abs(total-sum_inp)
    print(str(diff))
    ans=ans.lstrip()
    print(ans)