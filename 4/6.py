num = int(input())
s=""

for i in range(num+1):
    s=s+" "+s.join(str(i))

s=s.lstrip()

print(s)