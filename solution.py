import math
def my_program():
    try:
        b = float(input("Введите число b: "))
        d = float(input("Введите число d: "))
        x = float(input("Введите число x: "))
        y = 0
    except ArithmeticError:
        print("Неправильно введенные данные!")
    try:
        if x >= 8 :
            y = (x-2)/(x*x)
        else:
            y = ((b*b)*d) + (4*math.pow(x,3))
        print("y = " , y)
    except ArithmeticError:
        print("Нет ответа!")