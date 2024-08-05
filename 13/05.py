num = int(input())

months = {
    'янв': [],
    'фев': [],
    'мар': [],
    'апр': [],
    'май': [],
    'июн': [],
    'июл': [],
    'авг': [],
    'сен': [],
    'окт': [],
    'ноя': [],
    'дек': [],
}

for _ in range(num):

    line = input().split()
    name = line[0]
    month = line[2]
    months[month].append(name)
    months[month].sort()

for _ in range(int(input())):
    month = input()
    print(' '.join(months[month]))
