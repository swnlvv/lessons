line=input().upper()
words=line.split()

for i in range(len(words)):
    print('-'.join(words[i]), end=' ')