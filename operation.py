import random
class Operation:
    operation = None

    def __init__(self):
        self.answer = None

    def get_question(self,operation=operation):
        self.operation = operation
        a = random.randint(0,500)
        b = random.randint(1,500)
        if self.operation == "addition":
            self.answer = a + b
            return "Combien font {} + {}".format(a,b)
        if self.operation == "soustraction":
            self.answer = a - b
            return "Combien font {} - {}".format(a,b)
        if self.operation == "multiplication":
            self.answer = a * b
            return "Combien font {} * {}".format(a,b)
        if self.operation == "division":
            self.answer = a // b
            return "Combien font {} / {} (division entière)".format(a,b)

    def get_answer(self):
        return self.answer
