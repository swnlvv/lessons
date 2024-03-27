days=0

temp=float(input())

while temp<22:

    days+=1

    temp=float("".join(input()))

print(days // 7)