numbers=[]

for i in range(17):
    numbers.append(int(input()))
print("ДА")
for i in range(1, 17):
    
    if i%numbers[i]==0:
        print("ДА")
    else:
        print("НЕТ")