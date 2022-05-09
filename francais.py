import random


class Francais:
    types = None

    def __init__(self):
        self.index = 0
        # première colonne : question, deuxième colonne : réponse
        # index 0:2 : présent de l'indicatif, index 3:5 : imparfait
        self.liste_conjugaison = [["Je ___ (boire) une limonade", "Le chien ___ (aboyer) à la barrière",
                                   "Les enfants ___ (jouer) dans le jardin.",
                                   "Les randonneurs ___ (faire) un feu, lorsque le garde est arrivé.",
                                   " À cette date, l'an dernier, mes parents ___ (déménager).",
                                   " Chaque dimanche, tu nous ___ (préparer) un bon gâteau."],
                                  ["bois", "aboie", "jouent", "faisaient", "déménagaient", "préparais"]]
        # la première colonne correspond à la question, la deuxième aux réponses possibles, la troisième à la bonne réponse
        # index 0-2 : conj. de subord.,
        self.liste_grammaire = [["Il aimerait ___ je l'accompagne.", "La mer se déchaine ___ le vent souffle beaucoup.",
                                 "___tu n’es pas d’accord, il suffit de le dire."],
                                [["dès que", "lorsque", "que"], ["comme", "lorsque", "que"],
                                 ["Avant que", "Si", "Que"]],
                                ["que", "lorsque", "Si"]]
        # la première colonne correspond à la question, la deuxième aux réponses possibles, la troisième à la bonne réponse
        # index 0-2 : homonymes
        self.liste_orthographe = [["Certains lutins utilisent plutôt ___ nombreux pouvoirs pour aider les bonnes gens.",
                                   "Je porte une ___ à l'annulaire.", "Jean me ___ dans une position délicate."],
                                  [["leurs", "leur", "l'heure", "leurre"], ["bage", "bague"],
                                   ["mets", "met", "mais", "m'est"]],
                                  ["leurs", "bague", "met"]]
        # la première colonne correspond à la question, la deuxième aux réponses possibles, la troisème les bonnes réponses mais dans l'odre
        # ce sont des synonymes

        self.liste_vocabulaire = [["solitaire", "ponctuel", "heureux", "mature", "lâche", "mauvais"],
                                  ["régulier", "jovial", "mûr", "déplaisant", "isolé", "poltron"],
                                  ["isolé", "régulier", "jovial", "mûr", "poltron", "déplaisant"]]
        self.liste_lecture = ["Nik a les cheveux courts.",
                              "Lisa a les cheveux longs.",
                              "Elle a les cheveux mi-longs.",
                              "Il a les cheveux raides.",
                              "Elle a les cheveux ondulés.",
                              "Tina a les cheveux bouclés.",
                              "Maria a les cheveux couleur noisette.",
                              "Peter a les cheveux noirs.",
                              "Oli est blonde.",
                              "Rosi est rousse.",
                              "Il a les yeux marron.",
                              "Elle a les yeux verts.",
                              "Il a les yeux bleus.",
                              "Elle est mate de peau.",
                              "Il a le teint clair.",
                              "Elle est petite.",
                              "Il est grand.",
                              "Elle est mince.",
                              "Il est gros.",
                              "Il est maigre.",
                              "Elle est rapide.",
                              "Il est lent.",
                              "Elle est forte.",
                              "Elle est faible",
                              "Elle est jolie.",
                              "Il est beau.",
                              "Il est mignon.",
                              "Elle est laide",
                              "Elle est amicale.",
                              "Il est gentil.",
                              "Elle est calme.",
                              "Elle est timide.",
                              "Il a de l‘humour.",
                              "Elle est intelligente.",
                              "Il est patient.",
                              "Elle est paresseuse.",
                              "Il est mal élevé.",
                              "Il est sérieux.",
                              "Il est agréable",
                              "Elle travaille dur.",
                              "Il est sophistiqué.",
                              "Elle est courageuse.",
                              "Il est marrant.",
                              "Elle est pauvre.",
                              "Elle est riche.",
                              "Fais attention.",
                              "Fais attention en conduisant.",
                              "Est-ce que tu peux traduire ça pour moi?",
                              "Chicago est très différente de Boston.",
                              "Ne t'inquiète pas.",
                              "Tout le monde le sais.",
                              "Tout est prêt.",
                              "Excellent.",
                              "De temps en temps.",
                              "Bonne idée.",
                              "Il l'aime beaucoup.",
                              "A l'aide!",
                              "Il arrive bientôt.",
                              "Il a raison.",
                              "Il est très ennuyeux.",
                              "Il est très célèbre.",
                              "Comment ça va?",
                              "Comment va le travail?",
                              "Dépêche-toi!",
                              "J'ai déjà mangé.",
                              "Je ne vous entends pas.",
                              "Je voudrais faire une promenade.",
                              "Je ne sais pas m'en servir.",
                              "Je ne l'aime pas.",
                              "Je ne l'aime pas.",
                              "Je ne parle pas très bien.",
                              "Je ne comprends pas.",
                              "Je n'en veux pas.",
                              "Je ne veux pas ça.",
                              "Je ne veux pas te déranger.",
                              "Je me sens bien.",
                              "Si vous avez besoin de mon aide, faites-le-moi savoir s'il vous plaît.",
                              "Je sors du travail à six heures.",
                              "J'ai mal à la tête.",
                              "J'espère que vous ferez un bon voyage.",
                              "Je sais.",
                              "Je l'aime.",
                              "Je t'appellerai vendredi.",
                              "Je reviendrai plus tard.",
                              "Je paierai.",
                              "Je vais le prendre.",
                              "Je t’emmènerai à l'arrêt de bus.",
                              "J'ai perdu ma montre.",
                              "Je t'aime.",
                              "Je suis un Américain.",
                              "Je nettoie ma chambre.",
                              "J'ai froid.",
                              "Je viens te chercher.",
                              "Je vais partir.",
                              "Je vais bien, et toi?",
                              "Je suis content.",
                              "J'ai faim.",
                              "Je suis marié.",
                              "Je ne suis pas occupé.",
                              "Je ne suis pas marié.",
                              "Je ne suis pas encore prêt.",
                              "Je ne suis pas sûr.",
                              "Je suis désolé, nous sommes complets.",
                              "J'ai soif.",
                              "Je suis très occupé. Je n'ai pas le temps maintenant.",
                              "J'ai besoin de changer de vêtements.",
                              "J'ai besoin d'aller chez moi.",
                              "Je veux seulement un en-cas.",
                              "Est-ce que Monsieur Smith est un Américain?",
                              "Est-ce que ça suffit?",
                              "Je pense que c'est très bon.",
                              "Je pense que c'est bon.",
                              "Je pensais que les vêtements étaient plus chers.",
                              "C'est plus long que deux kilomètres.",
                              "Je suis ici depuis deux jours.",
                              "J'ai entendu dire que le Texas était beau comme endroit.",
                              "Je n'ai jamais vu ça avant.",
                              "J'allais quitter le restaurant quand mes amis sont arrivés.",
                              "Juste un peu.",
                              "Juste un moment.",
                              "Laisse-moi vérifier.",
                              "laisse-moi y réfléchir.",
                              "Allons voir.",
                              "Pratiquons l'anglais.",
                              "Pourrais-je parler à madame Smith s'il vous plaît?",
                              "Plus que ça.",
                              "Peu importe.",
                              "La prochaine fois.",
                              "Non.",
                              "N'importe quoi.",
                              "Non, merci.",
                              "Rien d'autre.",
                              "Pas récemment.",
                              "Pas encore.",
                              "Bien sûr.",
                              "D'accord.",
                              "S'il vous plaît remplissez ce formulaire.",
                              "S'il vous plaît emmenez-moi à cette adresse.",
                              "S'il te plaît écris-le.",
                              "Vraiment?",
                              "Juste ici.",
                              "Juste là.",
                              "A bientôt.",
                              "A demain.",
                              "A ce soir.",
                              "Elle est jolie.",
                              "Désolé de vous déranger.",
                              "Arrête!",
                              "Tente ta chance.",
                              "Réglez ça dehors.",
                              "Dis-moi.",
                              "Merci pour tout.",
                              "Merci pour ton aide.",
                              "Merci.",
                              "Merci Mademoiselle.",
                              "Merci Monsieur.",
                              "Merci beaucoup.",
                              "Ça a l'air super.",
                              "C'est pas mal.",
                              "Ça suffit.",
                              "C'est bon.",
                              "C'est tout.",
                              "Ça sent mauvais.",
                              "Ce n'est pas juste.",
                              "Ce n'est pas vrai.",
                              "C'est vrai.",
                              "C'est dommage.",
                              "C'est trop.",
                              "C'est trop.",
                              "Le livre est sous la table.",
                              "Ils vont revenir tout de suite.",
                              "Ce sont les mêmes.",
                              "Ils sont très occupés.",
                              "Ça ne marche pas.",
                              "C'est très difficile.",
                              "C'est très important.",
                              "Essaie-le/la.",
                              "Très bien, merci.",
                              "Nous l'aimons beaucoup.",
                              "Voudriez-vous prendre un message s'il vous plaît?"
                              ]

    def get_question2(self):
        if self.types == "vocabulaire":
            return "[i]" + self.liste_vocabulaire[0][self.index] + "[/i]" + "\n" + "/".join(self.liste_vocabulaire[1])
        if self.types == "grammaire":
            return "[i]" + self.liste_grammaire[0][self.index] + "[/i]" + "\n" + " ".join(
                self.liste_grammaire[1][self.index])
        if self.types == "orthographe":
            return "[i]" + self.liste_orthographe[0][self.index] + "[/i]" + "\n" + " ".join(
                self.liste_orthographe[1][self.index])
        if self.types == "conjugaison":
            return "[i]" + self.liste_conjugaison[0][self.index] + "[/i]"

    def get_question(self, types=types):
        self.types = types
        if self.types == "conjugaison":
            self.index = random.randint(0, len(self.liste_conjugaison[0]) - 1)
            if self.index < 3:
                return "[b]Complète la phrase en conjugant le verbe entre parenthèses au présent de l'indicatif.[/b]" + "\n" + "[i]" + \
                       self.liste_conjugaison[0][self.index] + "[/i]"
            else:
                return "[b]Complète la phrase en conjugant le verbe entre parenthèses à l'imparfait.[/b]" + "\n" + "[i]" + \
                       self.liste_conjugaison[0][self.index] + "[/i]"
        if self.types == "grammaire":
            self.index = random.randint(0, len(self.liste_grammaire[0]) - 1)
            return "[b]Complète la phrase avec la bonne conjonction de subodinnation.[/b]" + "\n" + "[i]" + \
                   self.liste_grammaire[0][self.index] + "[/i]" + "\n" + " ".join(
                self.liste_grammaire[1][self.index])
        if self.types == "orthographe":
            self.index = random.randint(0, len(self.liste_orthographe[0]) - 1)
            return "[b]Complète la phrase avec le bon mot[/b]" + "\n" + "[i]" + self.liste_orthographe[0][
                self.index] + "[/i]" + "\n" + " ".join(
                self.liste_orthographe[1][self.index])
        if self.types == "vocabulaire":
            self.types = "vocabulaire"
            self.index = random.randint(0, len(self.liste_vocabulaire[0]) - 1)
            return "[b]Associe le mot à son synonyme[/b]" + "\n" + "[i]" + self.liste_vocabulaire[0][
                self.index] + "[/i]" + "\n" + "/".join(self.liste_vocabulaire[1])
        if self.types == "lecture":
            self.types = "lecture"
            self.index = random.randint(0, len(self.liste_lecture) - 1)
            return "[b] Lisez la phrase : " + "[i]" + self.liste_lecture[self.index] + "[/i][/b]"

    def check_reponse(self,sim=0):
        if self.types == "vocabulaire":
            if self.answer_text.text == self.liste_vocabulaire[2][self.index]:
                print("Bien joué")
                return True
            else:
                print("Dommage")
                return False
        if self.types == "grammaire":
            if self.answer_text.text == self.liste_grammaire[2][self.index]:
                print("Bien joué")
                return True
            else:
                print("Dommage")
                return False
        if self.types == "orthographe":
            if self.answer_text.text == self.liste_orthographe[2][self.index]:
                print("Bien joué")
                return True
            else:
                print("Dommage")
                return False
        if self.types == "conjugaison":
            if self.answer_text.text == self.liste_conjugaison[1][self.index]:
                print("Bien joué")
                return True
            else:
                print("Dommage")
                return False
        if self.types == "lecture":
            if sim>0.9:
                print("Bien joué")
                return True
            else:
                return False
            pass
