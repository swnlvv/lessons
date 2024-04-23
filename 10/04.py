n = int(input())

lines=[]
for _ in range(n):
    lines.append(input())

for i in range(n-1):
    for j in range(n-1-i):
        if len(lines[j])>len(lines[j+1]):
            lines[j], lines[j+1]=lines[j+1], lines[j]
        elif len(lines[j])==len(lines[j+1]):
            if lines[j]>lines[j+1]:
                lines[j], lines[j+1]=lines[j+1], lines[j]

for i in lines:
    print(i)