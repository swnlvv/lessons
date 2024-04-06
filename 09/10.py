n=int(input())

inp=list()

for _ in range(n):
    inp.append(int(input()))

start=int(input())-1
end=int(input())

summ=0

for x in range(start, end):
    summ+=inp[x]

print(summ)