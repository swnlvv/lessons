
s="1"
num=int(input())

for _ in range(2, num):
    
    if num%_ ==0:
        s+=" "+s.join(str(_))
        print(_)
check = set(s)
s+=" "+str(num)
if len(check)>3:        #два делителя для чека на простое число + компенсация пробела в сете, тк числа выводятся через пробел
    print("НЕТ")
else:
    print("ДА")
print(s)
