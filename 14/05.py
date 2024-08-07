def triangle(a, b, c):
    if (a+b)<=c:
        print("Это не треугольник")
    elif (a+c)<=b:
        print("Это не треугольник")
    elif (b+c)<=a:
        print("Это не треугольник")
    else:
        print("Это треугольник")
