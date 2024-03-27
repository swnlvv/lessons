money=int(input())

oct_money=oct(money)

##компенсируется наличие префикса 0о при переводе в восьмиричную систему счисления

print(str(oct_money)[2])