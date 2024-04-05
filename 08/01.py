s=input()
wordlist=[]
while s!='стоп':
    wordlist.append(s)
    s=input()

minlen=wordlist[0]
maxlen=wordlist[0]


for word in wordlist:
    if len(word)<len(minlen):
        minlen=word
    elif len(word)>len(maxlen):
        maxlen=word

minset=set()

for letter in minlen:
    minset.add(letter)

maxset=set()

for letter in maxlen:
    maxset.add(letter)

ans=True

for letter in minset:
    if letter not in maxset:
        ans=False
        break

if ans==True:
    print('ДА')
else:
    print('НЕТ')