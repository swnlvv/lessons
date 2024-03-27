min=1

max=1000

n=0


def binary_search(min, max):

    global n


    median=int((max+min)/2)

    print(median)

    oper=str(input())

    if oper=="=":

        pass

    while (oper!="=")&(n<10):



        if oper==">":

            min=median

            binary_search(min, max)

            n+=1

        else:

            max=median
            binary_search(min, max)
            n+=1


binary_search(min, max)