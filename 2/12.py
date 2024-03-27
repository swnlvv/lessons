sentence=str(input())

l=len(sentence)

price=l*0.4

rub, kop =divmod(price, 1)

rub=int(rub)

kop=int(kop*100)

print(f"{rub} р. {kop} коп.")