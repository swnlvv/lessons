bull=0
cow=0

s=input()
s1=input()


s1set=set(s1)

for i in range(len(s)):
    if s[i]==s1[i]:
        bull+=1
    elif s[i] in s1set:
        cow+=1

print(bull, cow)