def print_average(arr):
    if len(arr)==0:
        print('0')
        return
    else:
        summ = 0
        for item in arr:
            summ+=item
        print(round((summ/len(arr)), 1))
