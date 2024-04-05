s = input()

max_o=0
o=0
for letter in s:
    if (letter=='o') or (letter=='о'):              #англ и ру раскладки, в задаче не уточнено
        o+=1
        if o>max_o:
            max_o=o
    else:
        o=0

print(max_o)