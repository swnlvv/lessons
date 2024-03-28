german=set()
english=set()

num_eng=int(input())
num_ger=int(input())

for i in range(num_eng):
    english.add(input())
for i in range(num_ger):
    german.add(input())

biling=0

if len(german)>len(english):
    for eng in english:
        if eng in german:
            biling+=1

else:
    for ger in german:
        if ger in english:
            biling+=1

ans=num_eng+num_ger-2*biling
if ans==0:
    print('NO')
else:
    print(ans)
