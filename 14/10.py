def golden_ratio(i):
    a = 1
    b = 1
    n = 0
    while n < i - 2:
        summ = a + b
        a = b
        b = summ
        n+=1
        
    summ = a+b
    ans=summ/b
    print(ans)
    
golden_ratio(4)