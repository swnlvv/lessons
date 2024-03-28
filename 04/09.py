n=int(input())
space=" "
symb="*"
for i in range(n):
    space_out=space*(n-i-1)
    symbols_out=symb*(i*2+1)
    print(space_out+symbols_out)