import ast
import operator as op
from random import randint

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


# source https://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string
def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)


def seperate_string_number(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
    return groups


# source : https://stackoverflow.com/questions/430079/how-to-split-strings-into-text-and-number
class Inversee():
    def __init__(self):
        self.difficulte = "FACILE"
        self.resultat = 0
        self.score = 0
        self.vie = 3
        self.reponse = 0

    def get_question(self):
        nombre = randint(1, 500)
        print("Donnez une combinaison pour trouver le nombre : ", nombre)
        self.reponse = nombre
        return nombre

    def get_rep(self,rep):
        return eval_expr(rep)

    def get_answer(self):
        return self.reponse


class Difficile:
    def __init__(self):
        self.difficulte = "DIFFICILE"
        self.resultat = 0
        self.score = 0
        self.vie = 3
        self.reponse = 0

    def get_question(self):
        nbre_op = randint(2, 5)
        nombre = randint(50, 1000)
        self.reponse = [nbre_op,nombre]
        return [nbre_op,nombre]

    def get_answer(self):
        return self.reponse

    def get_rep(self,rep):
        return eval_expr(rep)


class Compte:
    def __init__(self):
        self.difficulte = "DIFFICILE"
        self.resultat = 0
        self.score = 0
        self.vie = 3
        self.reponse = 0
        self.liste = []

    def get_liste(self):
        liste_nombres = []
        for i in range(0, 4):
            liste_nombres.append(randint(1, 30))
        nombre = liste_nombres[0]
        print(liste_nombres)
        for i in range(0, 3):
            x = randint(1, 3)
            print(x)
            if x == 1:
                nombre = nombre + liste_nombres[i + 1]
            elif x == 2:
                if nombre - liste_nombres[i + 1] < 0:
                    i -= 1
                    continue
                nombre = nombre - liste_nombres[i + 1]
            elif x == 3:
                nombre = nombre * liste_nombres[i + 1]
            self.reponse = nombre
            self.liste = liste_nombres
        return nombre,liste_nombres

    def get_question(self):
        return self.reponse

    def get_l(self):
        return self.liste

    def get_answer(self):
        return self.reponse

    def get_rep(self,rep):
        return eval_expr(rep)

"""
if __name__ == '__main__':
    difficulte = "FACILE"
    resultat = 0
    score = 0
    vie = 3
    while True:
        while True:
            print("Choisissez entre le mode facile, normal et difficile.\n")
            difficulte = input()
            difficulte = difficulte.upper()
            print(difficulte)
            if difficulte != "FACILE" and difficulte != "NORMAL" and difficulte != "DIFFICILE":
                print("Vous devez choisir entre facile, normal et difficile.")
                continue
            break

        if difficulte == "FACILE":
            nombre = randint(1, 500)
            while True:
                print("Donnez une combinaison pour trouver le nombre : ", nombre)
                a = input()
                resultat = eval_expr(a)
                print("Vous avez trouvé :", resultat)
                if resultat == nombre:
                    score += 1
                    print("Félicitations, vous avez trouvé", score, "des possibilités sur 3")
                    nombre = randint(1, 500)
                    if score == 3:
                        print("Vous avez trouver toutes les combinaisons nécessaires, vous pouvez passer au niveau "
                              "suivant.")
                        difficulte = "NORMAL"
                        score = 0
                        vie = 3
                        break
                    continue

                else:
                    vie -= 1
                    print("Malheureusement, cette combinaison ne marche pas. Il ne vous reste que", vie, "vies")
                    if vie == 0:
                        print("Dommage, il ne vous reste plus de vies ! Réessayez une prochaine fois.")
                        break

        elif difficulte == "NORMAL":
            nbre_op = randint(2, 5)
            nombre = randint(50, 1000)
            while True:
                print("Vous devez trouver le nombre", nombre, "avec exactement", nbre_op, "nombres.")
                if vie == 0:
                    print("Dommage, il ne vous reste plus de vies ! Réessayez une prochaine fois.")
                    break

                print("Ecrivez vos opération")
                a = input()
                resultat = eval_expr(a)
                a = seperate_string_number(a)
                compteur = 0
                for i in a:
                    try:
                        i = int(i)
                    except Exception:
                        pass
                    if isinstance(i, int):
                        compteur += 1
                if compteur != nbre_op:
                    vie -= 1
                    print("Vous n'avez pas utiliser la bonne quantité de nombres ! Vous perdez une vie. Il ne vous en "
                          "reste que", vie)
                    continue

                if resultat == nombre:
                    score += 1
                    print("Félicitations, vous avez trouvé", score, "des possibilités sur 3")
                    nombre = randint(50, 1000)
                    if score == 3:
                        print("Vous avez trouver toutes les combinaisons nécessaires, vous pouvez passer au niveau "
                              "suivant.")
                        score = 0
                        vie = 3
                        break
                    continue
                else:
                    vie -= 1
                    print("Malheureusement, cette combinaison ne marche pas. Il ne vous reste que", vie, "vies")

        elif difficulte == "DIFFICILE":
            liste_nombres = []
            for i in range(0, 4):
                liste_nombres.append(randint(1, 30))
            nombre = liste_nombres[0]
            print(liste_nombres)
            for i in range(0, 3):
                x = randint(1, 3)
                print(x)
                if x == 1:
                    nombre = nombre + liste_nombres[i + 1]
                elif x == 2:
                    if nombre - liste_nombres[i + 1] < 0:
                        i -= 1
                        continue
                    nombre = nombre - liste_nombres[i + 1]
                elif x == 3:
                    nombre = nombre * liste_nombres[i + 1]

            print("Les règles ici sont quelques peu différentes. A partir d'une liste de nombres, vous devez "
                  "retrouver le nombre cherché en une quantité d'opérations limitée, avec uniquement les additions, "
                  "les soustractions, et les multiplications.")
            print("Vous devez trouver le nombre", nombre, "avec uniquement les nombres suivants :", liste_nombres,
                  "en exactement 3 opérations")
            while True:
                if vie == 0:
                    print("Dommage, il ne vous reste plus de vies ! Réessayez une prochaine fois.")
                    break

                print("Ecrivez vos opération")
                a = input()
                resultat = eval_expr(a)
                print("Vous avez trouvé :", resultat)
                a = seperate_string_number(a)
                compteur = 0
                for i in a:
                    try:
                        i = int(i)
                    except Exception:
                        pass
                    if isinstance(i, int):
                        if int(i) not in liste_nombres:
                            print("Vous ne devez utiliser que des valeurs présentes dans la liste suivante :",liste_nombres)
                            vie -= 1
                            print("Vous perdez une vie. Il ne vous en reste que",vie)
                            continue
                        compteur += 1
                if compteur != 4:
                    print("Vous n'avez pas utiliser la bonne quantité de nombres ! Vous perdez une vie. Il ne vous en "
                          "reste que", vie)
                    vie -= 1
                    continue

                if resultat == nombre:
                    print("Félicitations, vous avez trouvé la solution !")
                    break
                else:
                    vie -= 1
                    print("Malheureusement, cette combinaison ne marche pas. Il ne vous reste que", vie, "vies")"""
