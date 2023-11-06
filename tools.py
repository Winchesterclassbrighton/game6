import random as rn


def slope(x1, x2, y1, y2):
    rise = y2-y1
    run = x2-x1
    m = rise/run
    return m


def y_intercept(x1, x2, y1, y2):
    m = slope(x1, x2, y1, y2)
    b = y1-m*x1
    return b


def generate_worksheet(title):
    def generate_slope_intercept():
        return "y = " + str(rn.randint(-9, 9)) + "x + " + str(rn.randint(-9, 9))

    def prompt_1():
        result = "Find an equation of a line that is parallel, an equation of a line that is perpendicular, \nand the"
        result += " x-intercept to the following line:  "
        return result

    string = title + "\n\n"
    for i in range(1, 30):
        string += str(i) + ")   "
        string += prompt_1()
        string += generate_slope_intercept()
        string += "\n\n\n\n\n\n"
    return string


def factorial_problem():
    def factorial(n):
        if n == 1:
            return 1
        return n*factorial(n-1)

    result = 0
    for i in range(100):
        result += factorial(i)
    return result


print(generate_worksheet("11/6 model worksheet"))
