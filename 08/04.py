letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']

n=int(input())
width=n
while n>0:
    for x in range(width):
        print(letters[x]+str(n), end=' ')
        
    print('\n')        
    n-=1