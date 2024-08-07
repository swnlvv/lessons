def quater(xcoord, ycoord):
    if (xcoord>0) and (ycoord>0):
        print('I четверть')
    elif (xcoord<0) and (ycoord>0):
        print("II четверть")
    elif (xcoord<0) and (ycoord<0):
        print("III четверть")
    elif (xcoord>0) and (ycoord<0):
        print('IV четверть')
    else:
        print("Точка лежит на оси координат")
    

quater(3, 4)
quater(-3.5, 8)