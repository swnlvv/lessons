white_list_num=int(input())
white_list=list()
for _ in range(white_list_num):
    white_list.append(input())

search_num=int(input())

search_list=list()

for _ in range(search_num):
    search_list.append(input())

for search in search_list:
    if search in white_list:
        print(search)