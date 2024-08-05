num = int(input())

d = {
     
}
  
for _ in range(num):
    line = input().split()
    word = line[0]
    description = line[1:len(line)+1]
    d[word] = description

for _ in range(int(input())):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print("Нет в словаре")