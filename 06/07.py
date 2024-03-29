first=set()
second=set()
first_num=int(input())
second_num=int(input())


for _ in range(first_num):
    first.add(input())

for _ in range(second_num):
    second.add(input())

if len(first)>len(second):
    for x in second:
        if x in first:
            print(x)
else:
    for x in first:
        if x in second:
            print(x)