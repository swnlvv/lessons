first=str(input())

second=str(input())



def check(first, second):

    i=0

    while i==0:

        if len(first)<8:

            print("Короткий!")

            first=str(input())

            second=str(input())

            check(first, second)

        elif "123" in first:

            print("Простой!")

            first=str(input())

            second=str(input())

            check(first, second)

        elif first!=second:

            print("Различаются")

            first=str(input())

            second=str(input())
            check(first, second)

        else:

            print("OK")

            i=1

check(first, second)