import random as rn


def get_primes(n):
    primes = [2]
    for i in range(3, n):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


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
    a = rn.randint(-9, 9)
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
#    print("__________________________________________________________________________________________________________")
#    print(a/c)
#    print(b/d)
#    print(q)
#    print(int(x) / int(y))
#    print("__________________________________________________________________________________________________________")
    if q == "+":
        if abs((int(x) / int(y)) - ((a / c) + (b / d))) < .00001:
            if check_for_full_reduction(int(x), int(y)):
                print("correct")
                return 1
            else:
                print("not fully reduced, GAME OVER!")
        else:
            print("incorrect, GAME OVER!")
            return 0
    elif q == "-":
        if abs((int(x) / int(y)) - ((a / c) - (b / d))) < .00001:
            if check_for_full_reduction(int(x), int(y)):
                print("correct")
                return 1
            else:
                print("not fully reduced, GAME OVER!")
        else:
            print("incorrect, GAME OVER!")
            print(((a / c) - (b / d)))
            return 0
    elif q == "\u22c5":
        if abs((int(x) / int(y)) - ((a * b) / (c * d))) < .00001:
            if check_for_full_reduction(int(x), int(y)):
                print("correct")
                return 1
            else:
                print("not fully reduced, GAME OVER!")
        else:
            print("incorrect, GAME OVER!")
            print((a * b) / (c * d))
            return 0
    elif q == "\u00f7":
        if abs((int(x) / int(y)) - ((a / c) / (b / d))) < 0.00001:
            if check_for_full_reduction(int(x), int(y)):
                print("correct")
                return 1
            else:
                print("not fully reduced, GAME OVER!")
        else:
            print("incorrect, GAME OVER!")
            print((a / c) / (b / d))
            return 0


def check_for_full_reduction(numerator, denominator):
    if numerator == 0:
        return True
    for i in get_primes(numerator):
        if numerator % i == 0:
            if denominator % i == 0:
                return False
    return True


def game():
    print("Welcome, challenger to win you must answer 10 correct in a row but if you get one wrong you lose\n\n\n"
          "")
    input("press enter when your ready to begin ...")
    for i in range(0, 10):
        score = 0
        if generate_problem() == 1:
            score += 1
        else:
            return 0
    print("you win!")
    return 0


def game7():
    print("Welcome Challenger, your goal is to leave these woods!")
    print("There are two paths ahead a path on the left and a path on the right,")
    q1 = input("if you wish to take the path on the left type \"left\" and "
               "press enter otherwise type \"right\" then press enter.")
    if q1 == "left":
        print("You have found a map. There are three paths ahead but the map suggests two are deadly!")
        print("One path leads to a den of venomous snakes the other leads to sheer cliffs.")
        print("")
    elif q1 == "right":
        pass
    else:
        print("Your indecisiveness has gotten you mauled by a bear! Game Over.")


def generate_one_digit():
    return rn.randint(-9, 9)


class Expression:
    def __init__(self, terms):
        self.terms = terms


class Term:
    def __init__(self, var, coefficient):
        self.var = var
        self.coefficient = coefficient

    def __add__(self, other):
        if self.var == other.var:
            return Term(self.var, self.coefficient + other.coefficient)
        else:
            pass

    def __repr__(self):
        if self.coefficient >= 0:
            return "+" + str(self.coefficient) + self.var
        return str(self.coefficient) + self.var


def random_term():
    return Term("x", generate_one_digit())


def combining_like_terms_problem(diff):
    a = []
    promt = ""
    result = 0
    for i in range(0, rn.randint(4, 4 + diff)):
        q = random_term()
        a.append(q)
        promt += q.__repr__()
        result += q.coefficient
    print("Given the following expression combine like terms to give the simplified expression, \n" + promt)
    b = input("type the coefficient in the simplified expression then press enter.")
    if abs(b - result) < .0001:
        print("Correct!")
        return 1
    else:
        print("Incorrect, GAME OVER!")
        return 0


game()




