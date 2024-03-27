a, b=float(input()), float(input())

oper=str(input())

operators=["-", "+", "/", "*"]

if (oper not in operators) or ((oper=="/") and (b==0)):

    print(888888)

else:

    if oper=="-":

        print(a-b)

    elif oper=="+":

        print(a+b)

    elif oper=="/":

        print(a/b)

    else:

        print(a*b)