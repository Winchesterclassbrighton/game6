import random as rn


def game():
    print(Welcome Challenger, your goal is to leave these woods! \n There are two paths ahead a path on the left and a path on the right, \n)
    q1 = input("if you wish to take the path on the left type \"left\" and press enter otherwise type \"right\" then press enter.")
    if q1 == "left":
        print("You have found a map. There are three paths ahead but the map suggests two are deadly! \n One path leads to a den of venomous snakes the other leads to sheer cliffs.")
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
        if self.var = other.var:
            return Term(self.var, self.coefficient+other.coefficient)
        else:
            pass

    def __repr__(self):
        if self.coefficient >= 0:
            return "+"+str(self.coefficient)+self.var
        return str(self.coefficient)+self.var


def random_term():
    return Term("x", generate_one_digit())


def combining_like_terms(diff):
    a = []
    promt = ""
    result = 0
    for i in range(0, rn.randint(4, 4+diff)):
        q = random_term()
        a.append(q)
        promt += q.__repr__() 
        result += q.coefficient 
    print("Given the following expression combine like terms to give the simplified expression, \n"+promt)
    b = input("type the coefficient in the simplified expression then press enter.")
    if abs(b - result) < .0001:
        print("Correct!")
        return 1
    else:
        print("Incorrect, GAME OVER!")
        return 0
        




