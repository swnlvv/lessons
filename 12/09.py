s = input()

sentence = input().split()

for word in sentence:
    if s in word or s.upper() in word:
        print(word)