menu=['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']


n=int(input())

for x in range(n):
    print(menu[x%(len(menu))])