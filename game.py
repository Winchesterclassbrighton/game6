import random as rn


def generate_operation():
    n = rn.randint(1, 4)
    if n == 1:
        return "+"
    elif n == 2:
        return "-"
    elif n == 3:
        return "\u22C5"
    elif n == 4:
        return "\u00f7"


def generate_problem():
    a = rn.randint(1, 9)
    b = rn.randint(1, 9)
    c = rn.randint(1, 9)
    d = rn.randint(1, 9)
    q = generate_operation()
    string = str(a) + "     " + str(b) + "     a \n\u2014  " + q
    if q == "\u22c5":
        string = string + "  \u2009\u2014  =  \u2014 \n" + str(c) + "     " + str(d) + "     b"
    else:
        string = string + "  \u2014  =  \u2014 \n" + str(c) + "     " + str(d) + "     b"
    print(string)
    x = input("type in the value for a and press enter\n")
    y = input("type in the value for b and press enter\n")
    if q == "+":
        if (int(x) / int(y)) == ((a / c) + (b / d)):
            print("correct")
            return 1
        else:
            print("incorrect, GAME OVER!")
            return 0
    elif q == "-":
        if (int(x) / int(y)) == ((a / c) - (b / d)):
            print("correct")
            return 1
        else:
            print("incorrect, GAME OVER!")
            return 0
    elif q == "\u22c5":
        if (int(x) / int(y)) == ((a / c) * (b / d)):
            print("correct")
            return 1
        else:
            print("incorrect, GAME OVER!")
            return 0
    elif q == "\u00f7":
        if (int(x) / int(y)) == ((a / c) / (b / d)):
            print("correct")
            return 1
        else:
            print("incorrect, GAME OVER!")
            return 0


def game():
    print("Welcome, challenger to win you must answer 3 correct in a row but if you get one wrong you lose\n\n\n"
          "")
    input("press enter when your ready to begin ...")
    for i in range(0, 3):
        score = 0
        if generate_problem() == 1:
            score = score + 1
        else:
            return 0
    print("you win!")
    return 0


game()
