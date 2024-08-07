import math
def print_statistics(arr):
    if len(arr)==0:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
    else:
        #number of elements
        print(len(arr))
        #avg
        summ=0
        for item in arr:
            summ+=item
        print(round((summ/len(arr)), 1))
        #min
        print(round(min(arr),1))
        #max
        print(round(max(arr),1))
        #mediana
        if len(arr)%2!=0:
            l=len(arr)
            n = math.ceil(l/2)
            n-=1
            print(round(arr[n], 1))
        else:
            l = len(arr)
            n = l/2
            summ = arr[n-1]+arr[n]
            avg = round((summ/2), 1)
            print(avg)

