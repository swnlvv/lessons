n=int(input())

numbers = []

for x in range(n):
    numbers.append(int(input()))

check=int(input())
ans=False
for i in range(n):
    for j in range(i+1,n):
        if (numbers[i]*numbers[j])==check:
            ans=True

if ans:
    print('ДА')
else:
    print('НЕТ')