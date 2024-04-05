n=int(input())
text=str()
for i in range(n):
    rule=input()
    if ("не" in rule) or ('Не' in rule):
        text=text+rule[3:]+'\n'
    else:
        text=text+rule+'\n'

text=text[:-1]
print(text)