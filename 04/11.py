num=int(input())
numbers=[]
for i in range(num):
    numbers.append(int(input()))

print("0")
for i in range(1, num):
    if numbers[i]>numbers[i-1]:
        print(">")
    elif numbers[i]<numbers[i-1]:
        print("<")
    else:
        print("=")