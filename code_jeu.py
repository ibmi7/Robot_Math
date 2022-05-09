
from random import *

#Exercice 1
#Niveaux 1

score=0
for i in range (3):
    a=randint(0,10)
    b=randint(0,10)
    c=int(input(str(a)+"*"+str(b)+"=?"))
    if a*b==c:
        score=score+1
        print("bravo,score=",str(score))
    else:
        score=score-1
        print("faux,score=",str(score))
print("score : ", str(score))

#Niveaux 2
score=0
for i in range (5):
    a=randint(0,20)
    b=randint(0,20)
    c=int(input(str(a)+"*"+str(b)+"=?"))
    if a*b==c:
        score=score+1
        print("bravo,score=",str(score))
    else:
        score=score-1
        print("faux,score=",str(score))
print("score : ", str(score))


# Exercice 2
#Niveau 1
score=0
for i in range (10):
    a=uniform(0.0,10.0)
    a2=round(a,2)
    b=uniform(0.0,10.0)
    b2 = round(b, 2)
    c=float(input(str(a2)+"*"+str(b2)+"=?"))
    if a*b==c:
        score=score+1
        print("bravo,score=",str(score))
    else:
        score=score-1
        print("faux,score=",str(score))
print("score : ", str(score))

#Niveau 2
score=0
for i in range (15):
    a=uniform(0.0,20.0)
    a2=round(a,2)
    b=uniform(0.0,20.0)
    b2 = round(b, 2)
    c=float(input(str(a2)+"*"+str(b2)+"=?"))
    if a*b==c:
        score=score+1
        print("bravo,score=",str(score))
    else:
        score=score-1
        print("faux,score=",str(score))
print("score : ", str(score))



import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random


kivy.require('2.0.0')

class GameView(BoxLayout):
    def __init__(self):
        super(GameView,self).__init__()
        self.randomValue = random.randint(0,1000)

    def check_number(self):
        if int(self.answer_input.text) == self.randomValue:
            self.result_label.text = "Congrat"
            self.result_label.color = "#00EF0B"
            self.randomValue = random.randint(0,1000)

        elif int(self.answer_input.text) > self.randomValue:
            self.result_label.text = "Less"
            self.result_label.color = "#EF3E00"

        elif int(self.answer_input.text) < self.randomValue:
            self.result_label.text = "More"
            self.result_label.color = "#EF3E00"
class MathApp(App):
    def build(self):
        return GameView()

mathApp = MathApp()
mathApp.run()

