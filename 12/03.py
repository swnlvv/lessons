numbers=input().split()

line=input().split()

first=int(line[0])
second=int(line[1])
summ=0

for i in range (first, second+1):
    summ+=int(numbers[i])
    
print(summ)