from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals
from speech_recognition import Recognizer, Microphone
from operation import Operation
import time
from difflib import SequenceMatcher
import webbrowser
import random
from francais import Francais
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

from inversee import Inversee, Difficile, seperate_string_number, Compte

# Couleur de fond
Window.clearcolor = get_color_from_hex("#AB1239")

# Police d'écriture
LabelBase.register(name="Roboto", fn_regular="./fonts/Roboto-Thin.ttf", fn_bold="./fonts/Roboto-Medium.ttf",
                   fn_italic="./fonts/Roboto-Italic.ttf")

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

##################################################################


class RobotMathRoot(BoxLayout):
    facile_screen = ObjectProperty(None)
    difficile_screen = ObjectProperty(None)
    mult_screen = ObjectProperty(None)
    compte_screen = ObjectProperty()
    fr_screen = ObjectProperty()
    lecture_screen = ObjectProperty()

    def __init__(self, **kwargs):
        super(RobotMathRoot, self).__init__(**kwargs)
        # Liste de tous les écrans précédents
        self.screen_list = []
        self.math_popup = MathPopup()

    def changeScreen(self, next_screen):
        question = None

        if self.ids.robot_screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.robot_screen_manager.current)

        if next_screen == "a propos":
            self.ids.robot_screen_manager.current = "about_screen"
        elif next_screen == "[b]retour[/b]":
            if self.screen_list:  # le cas où il reste des écrans
                self.screen_list.pop()
                self.ids.robot_screen_manager.current = self.screen_list.pop()
        ###########################FRANCAIS#####################################
        elif next_screen == "français":
            self.ids.robot_screen_manager.current = "francais_screen"
        elif next_screen == "conjugaison":
            self.fr_screen.question_text.text = self.fr_screen.get_question("conjugaison")
            self.ids.robot_screen_manager.current = "fr_screen"
        elif next_screen == "grammaire":
            self.fr_screen.question_text.text = self.fr_screen.get_question("grammaire")
            self.ids.robot_screen_manager.current = "fr_screen"
        elif next_screen == "orthographe":
            self.fr_screen.question_text.text = self.fr_screen.get_question("orthographe")
            self.ids.robot_screen_manager.current = "fr_screen"
        elif next_screen == "vocabulaire":
            self.fr_screen.question_text.text = self.fr_screen.get_question("vocabulaire")
            self.ids.robot_screen_manager.current = "fr_screen"
        elif next_screen == "lecture":
            self.lecture_screen.question_text.text = self.fr_screen.get_question("lecture")
            self.ids.robot_screen_manager.current = "lecture_screen"

        ###########################MATH#####################################
        elif next_screen == "math":
            self.ids.robot_screen_manager.current = "math_screen"
        elif next_screen == "addition":
            self.op_screen.question_text.text = self.op_screen.get_question("addition")
            self.ids.robot_screen_manager.current = "op_screen"
        elif next_screen == "soustraction":
            self.op_screen.question_text.text = self.op_screen.get_question("soustraction")
            self.ids.robot_screen_manager.current = "op_screen"
        elif next_screen == "multiplication":
            self.op_screen.question_text.text = self.op_screen.get_question("multiplication")
            self.ids.robot_screen_manager.current = "op_screen"
        elif next_screen == "division":
            self.op_screen.question_text.text = self.op_screen.get_question("division")
            self.ids.robot_screen_manager.current = "op_screen"
        #elif next_screen == "multiplication":
            #self.ids.robot_screen_manager.current = "mult_screen"
        elif next_screen == "le compte est bon":
            question = self.compte_screen.get_liste()
            self.compte_screen.question_text.text = RobotMathRoot.prepQuestion(question)
            self.ids.robot_screen_manager.current = "compte_screen"

        elif next_screen == "facile":
            question = self.facile_screen.get_question()
            self.facile_screen.question_text.text = RobotMathRoot.prepQuestion(question)
            self.ids.robot_screen_manager.current = "facile_screen"

        elif next_screen == "difficile":
            question = self.difficile_screen.get_question()
            self.difficile_screen.question_text.text = RobotMathRoot.prepQuestion(question)
            self.ids.robot_screen_manager.current = "difficile_screen"

        else:
            self.facile_screen.question_text.text = next_screen
            self.ids.robot_screen_manager.current = "diff_screen"

    @staticmethod
    def prepQuestion(question):
        if isinstance(question, list):
            return "Trouvez le nombre " + str(question[1]) + "\nen seulement " + str(question[0]) + " opérations."
        if isinstance(question, tuple):
            return "Trouvez le nombre " + str(question[0]) + "\navec seulement les nombres suivants:\n" + str(
                question[1])
        return "Trouvez le nombre " + str(question)

    def onBackBtn(self):
        # Vérifie s'il y a un écran vers lequel retourner
        if self.screen_list:  # le cas où il reste des écrans
            self.ids.robot_screen_manager.current = self.screen_list.pop()
            return True
        return False  # le cas où il n'en reste plus


##################################################################
class MultScreen(Screen):
    score = 0

    def __init__(self, **kwargs):
        super(MultScreen, self).__init__(**kwargs)
        self.randomValue = random.randint(0, 10)
        self.randomValue2 = random.randint(0, 10)
        self.resultat = self.randomValue * self.randomValue2
        # self.result_label.text = str(self.randomValue) + "*" + str(self.randomValue2) + "=?"
        # print(self.resultat)

    def check_number(self):
        # for i in range(3):

        if int(self.answer_input.text) == self.resultat:
            MultScreen.score += 1
            self.result_label.text = str(MultScreen.score)
            self.result_label.color = "#0065EF"
            self.randomValue = random.randint(0, 10)
            self.randomValue2 = random.randint(0, 10)
            self.resultat = self.randomValue * self.randomValue2
            self.result_label.text = str(self.randomValue) + "*" + str(self.randomValue2) + "=?"
            print("ok")


        elif int(self.answer_input.text) != self.resultat:
            MultScreen.score -= 1
            self.result_label.text = str(MultScreen.score)
            self.result_label.color = "#00EF0B"
            self.randomValue = random.randint(0, 10)
            self.randomValue2 = random.randint(0, 10)
            self.resultat = self.randomValue * self.randomValue2
            self.result_label.text = str(self.randomValue) + "*" + str(self.randomValue2) + "=?"

        if MultScreen.score == 5:
            self.result_label.text = "Bravo"
        print(self.resultat)
        print(MultScreen.score)


##################################################################


class FrScreen(Screen, Francais):
    def __init__(self, *args, **kwargs):
        super(FrScreen, self).__init__(*args, **kwargs)

    def new_question(self):
        self.question_text.text = self.get_question("lecture")

    def ecoute(self):
        root = App.get_running_app().root
        recognizer = Recognizer()
        with Microphone() as source:
            print("[i]Réglage du bruit ambiant... Patientez...[/i]")
            root.lecture_screen.answer_text.text = "[i]Réglage du bruit ambiant... Patientez...[/i]"
            recognizer.adjust_for_ambient_noise(source)
            print("[i]Vous pouvez parler...[/i]")
            root.lecture_screen.answer_text.text = "[i]Vous pouvez parler...[/i]"
            recorded_audio = recognizer.listen(source)
            print("Enregistrement terminé !")
            root.lecture_screen.answer_text.text = "Enregistrement terminé !"
        # Reconnaissance de l'audio
        try:
            print("Reconnaissance du texte...")
            root.lecture_screen.answer_text.text = "Reconnaissance du texte..."
            text = recognizer.recognize_google(
                recorded_audio,
                language="fr-FR"
            )
            print("Vous avez dit : {}".format(text))
            root.lecture_screen.answer_text.text = "Vous avez dit : {}".format(text)
        except Exception as ex:
            print(ex)
        original = self.liste_lecture[self.index].lower()
        original.translate({ord(i): None for i in '.!?,'})
        if original[-1] == '.' or '!' or '?' or ',':
            original = original[:-1]
        similtitude = similar(original,text)
        print(original)
        self.answer_text.text = "Similtitude entre la phrase lue et la phrase prononcée :" + str(similtitude*100) + "%"
        print(self.answer_text.text)
        root.math_popup.open(self.check_reponse(similtitude))


    """"
    def question(self):
        root = App.get_running_app().root
        if self.types:
            root.fr_screen.vrai_question.text = self.get_question2()
        if self.types == "vocabulaire":
            root.fr_screen.vrai_question.text = "[i]" + self.liste_vocabulaire[0][self.index]+"[/i]" + "\n" + "/".join(self.liste_vocabulaire[1])
        if self.types == "grammaire":
            root.fr_screen.vrai_question.text = "[i]" + self.liste_grammaire[0][self.index]+"[/i]" + "\n" + " ".join(self.liste_grammaire[1][self.index])
        if self.types == "orthographe":
            root.fr_screen.vrai_question.text = "[i]" + self.liste_orthographe[0][self.index]+"[/i]" + "\n" + " ".join(self.liste_orthographe[1][self.index])
        if self.types == "conjugaison":
            root.fr_screen.vrai_question.text = "[i]" + self.liste_conjugaison[0][self.index]+"[/i]"
    """

    def check_answer(self):
        root = App.get_running_app().root
        root.fr_screen.question_text.text = root.fr_screen.get_question(self.types)
        return self.check_reponse()
        """
        if self.types == "vocabulaire":
            if self.answer_text.text == self.liste_vocabulaire[2][self.index]:
                print("Bien joué")
            else:
                print("Dommage")
            root.fr_screen.question_text.text = root.fr_screen.get_vocabulaire_question()

        if self.types == "grammaire":
            if self.answer_text.text == self.liste_grammaire[2][self.index]:
                print("Bien joué")
            else:
                print("Dommage")
            root.fr_screen.question_text.text = root.fr_screen.get_grammaire_question()

        if self.types == "orthographe":
            if self.answer_text.text == self.liste_orthographe[2][self.index]:
                print("Bien joué")
            else:
                print("Dommage")
            root.fr_screen.question_text.text = root.fr_screen.get_orthographe_question()

        if self.types == "conjugaison":
            if self.answer_text.text == self.liste_conjugaison[1][self.index]:
                print("Bien joué")
            else:
                print("Dommage")
            root.fr_screen.question_text.text = root.fr_screen.get_conjugaison_question()

        if self.types == "lecture":
            root.fr_screen.question_text.text = root.fr_screen.get_lecture_question()
        """


class MathPopup(Popup):
    GOOD = "{} :D"
    BAD = "{}. :("
    GOOD_LIST = "Super! Formidable! Correct! Excellent!".split()
    BAD_LIST = ["Dommage!", "Presque!", "Pas loin!"]
    message = ObjectProperty()
    wrapped_button = ObjectProperty

    def __init__(self, *args, **kwargs):
        super(MathPopup, self).__init__(*args, **kwargs)

    def open(self, correct=True):
        # Si bonne réponse, enlever le button si il est visible
        if self.wrapped_button in self.content.children:
            self.content.remove_widget(self.wrapped_button)

        # Message à afficher
        self.message.text = self._prep_text(correct)

        # popup
        super(MathPopup, self).open()
        if correct:
            Clock.schedule_once(self.dismiss, 1)
        else:
            Clock.schedule_once(self.dismiss, 2)

    def _prep_text(self, correct):
        if correct:
            index = random.randint(0, len(self.GOOD_LIST) - 1)
            return self.GOOD.format(self.GOOD_LIST[index])
        else:
            index = random.randint(0, len(self.BAD_LIST) - 1)
            return self.BAD.format(self.BAD_LIST[index])


##################################################################

class KeyPadOp(GridLayout):
    def __init__(self, *args, **kwargs):
        super(KeyPadOp, self).__init__(*args, **kwargs)
        self.cols = 3
        self.spacing = 10
        self.createButtons()

    def createButtons(self):
        _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,"", "GO!"]
        for num in _list:
            self.add_widget(Button(text=str(num), on_release=self.onBtnPress))

    def onBtnPress(self, btn):
        screen = App.get_running_app().root.ids.op_screen
        answer_text = screen.answer_text
        if btn.text != "GO!":
            answer_text.text += btn.text
        if btn.text == "GO!" and answer_text.text != "":
            answer = screen.get_answer()
            root = App.get_running_app().root
            if int(answer_text.text) == answer:
                root.math_popup.open(True)
                print("Bien joué")
            else:
                root.math_popup.open(False)
                print("Mauvaise réponse")
            # Effacer le reste et afficher la question qui suit
            answer_text.text = ""
            # Preparer à avoir de nouvelles question :
            root.op_screen.question_text.text = root.op_screen.get_question(root.op_screen.operation)


class KeyPad(GridLayout):

    def __init__(self, *args, **kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)
        self.cols = 3
        self.spacing = 10
        self.createButtons()

    def createButtons(self):
        _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "(", ")", "+", "-", "*", "", "GO!"]
        for num in _list:
            self.add_widget(Button(text=str(num), on_release=self.onBtnPress))

    def onBtnPress(self, btn):
        screen = App.get_running_app().root.ids.facile_screen
        answer_text = screen.answer_text

        if btn.text != "GO!":
            answer_text.text += btn.text
        if btn.text == "GO!" and answer_text.text != "":
            rep = screen.get_rep(answer_text.text)
            answer = screen.get_answer()
            root = App.get_running_app().root
            if rep == answer:
                root.math_popup.open(True)
                print("Bien joué")
            else:
                root.math_popup.open(False)
                print("Mauvaise réponse")
            # Effacer le reste et afficher la question qui suit
            answer_text.text = ""
            # Preparer à avoir de nouvelles question :
            question = root.facile_screen.get_question()
            root.facile_screen.question_text.text = RobotMathRoot.prepQuestion(question)


##################################################################


class KeyPadDifficile(GridLayout):

    def __init__(self, *args, **kwargs):
        super(KeyPadDifficile, self).__init__(*args, **kwargs)
        self.cols = 3
        self.spacing = 10
        self.createButtons()

    def createButtons(self):
        _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "(", ")", "+", "-", "*", "", "GO!"]
        for num in _list:
            self.add_widget(Button(text=str(num), on_release=self.onBtnPress))

    def onBtnPress(self, btn):
        screen = App.get_running_app().root.ids.difficile_screen
        answer_text = screen.answer_text

        if btn.text != "GO!":
            answer_text.text += btn.text
        if btn.text == "GO!" and answer_text.text != "":
            a = seperate_string_number(answer_text.text)
            compteur = 0
            for i in a:
                try:
                    i = int(i)
                except Exception:
                    pass
                if isinstance(i, int):
                    compteur += 1

            rep = screen.get_rep(answer_text.text)
            answer = screen.get_answer()
            root = App.get_running_app().root
            if compteur != answer[0]:
                root.math_popup.open(False)
                print("Le nombre d'opérations n'est pas le bon")
            if rep == answer[1]:
                root.math_popup.open(True)
                print("Bien joué")
            else:
                root.math_popup.open(False)
                print("Mauvaise réponse")
            # Effacer le reste et afficher la question qui suit
            answer_text.text = ""
            # Preparer à avoir de nouvelles question :
            question = root.difficile_screen.get_question()
            root.difficile_screen.question_text.text = RobotMathRoot.prepQuestion(question)


##################################################################

class KeyPadCompte(GridLayout):

    def __init__(self, *args, **kwargs):
        super(KeyPadCompte, self).__init__(*args, **kwargs)
        self.cols = 3
        self.spacing = 10
        self.createButtons()

    def createButtons(self):
        """"
        if App.get_running_app().root:
            math_screen = App.get_running_app().root.ids.compte_screen
            _list = math_screen.get_liste()[1] + ["+", "-", "*", "", "GO!"]
            for num in self._list:
                self.add_widget(Button(text=str(num), on_release=self.onBtnPress))
        """
        _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "(", ")", "+", "-", "*", "", "GO!"]
        for num in _list:
            self.add_widget(Button(text=str(num), on_release=self.onBtnPress))

    def onBtnPress(self, btn):
        screen = App.get_running_app().root.ids.compte_screen
        answer_text = screen.answer_text

        if btn.text != "GO!":
            answer_text.text += btn.text
        if btn.text == "GO!" and answer_text.text != "":
            root = App.get_running_app().root
            a = seperate_string_number(answer_text.text)
            compteur = 0
            for i in a:
                try:
                    i = int(i)
                except Exception:
                    pass
                if isinstance(i, int):
                    l = screen.get_l()
                    if int(i) not in l:
                        print("Vous ne devez utiliser que des valeurs présentes dans la liste suivante :")
                        root.math_popup.open(False)
                    compteur += 1
            if compteur != 4:
                print("Vous n'avez pas utiliser la bonne quantité de nombres ! Vous perdez une vie. Il ne vous en "
                      "reste que", )
                root.math_popup.open(False)
            rep = screen.get_rep(answer_text.text)
            answer = screen.get_answer()
            root = App.get_running_app().root
            if rep == answer:
                root.math_popup.open(True)
                print("Bien joué")
            else:
                root.math_popup.open(False)
                print("Mauvaise réponse")
            # Effacer le reste et afficher la question qui suit
            answer_text.text = ""
            # Preparer à avoir de nouvelles question :
            question = root.compte_screen.get_liste()
            root.compte_screen.question_text.text = RobotMathRoot.prepQuestion(question)


##################################################################

class OperationScreen(Screen,Operation):
    def __init__(self,*args,**kwargs):
        super(OperationScreen,self).__init__(*args,**kwargs)


class FacileScreen(Screen, Inversee):
    def __init__(self, *args, **kwargs):
        super(FacileScreen, self).__init__(*args, **kwargs)


class DifficileScreen(Screen, Difficile):
    def __init__(self, *args, **kwargs):
        super(DifficileScreen, self).__init__(*args, **kwargs)


class CompteScreen(Screen, Compte):
    def __init__(self, *args, **kwargs):
        super(CompteScreen, self).__init__(*args, **kwargs)


##################################################################


class RobotMathApp(App):
    def __init__(self, **kwargs):
        super(RobotMathApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        # lorsque l'utilisateur appuies sur ECHAP
        if key == 27:
            return self.root.onBackBtn()

    def build(self):
        return RobotMathRoot()

    def getText(self):
        return ("Bienvenue dans l'app Robot Pédagogique !\n"
                "Cette app a été créée à l'aide du youtubeur [b][ref=yt]Daniel Gopar[/ref][/b]\n"
                "ainsi qu'à l'aide de [b][ref=kivy]kivy[/ref][/b]\n"
                "Un grand merci à Daniel Gopar et à sa suite de [b][ref=video]vidéos[/ref][/b] sur Math Tutor")

    def on_ref_press(self, instance, ref):
        _dict = {
            "kivy": "https://kivy.org/#home",
            "yt": "https://www.youtube.com/channel/UCCRdRbI93UGW0AZttVH3SbA",
            "video": "https://www.youtube.com/watch?v=qVL05_-Bmok&list=PL3kg5TcOuFlqHsEtDKneH56oHypWdHXwj"
        }

        webbrowser.open(_dict[ref])


if __name__ == '__main__':
    RobotMathApp().run()
