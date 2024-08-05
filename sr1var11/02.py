first_line = set(input().split())
second_line= set(input().split())
third_line= set(input().split())

return_line=""
return_list=[]

for item in second_line:
    if (item not in first_line)&(item not in third_line):
        return_list.append(item)
        return_line+=item+'-'

return_line=return_line[:-1]

min_length=len(return_list[0])

for item in return_list:
    if len(item)<min_length:
        min_length=len(item)

print(return_line)
print(min_length)