from forme import Forme
import turtle

class Carre(Forme):
    def __init__(self, cote, couleur):
        super().__init__(couleur)
        self.cote = cote

    def dessiner(self):
        turtle.color(self.couleur)
        turtle.begin_fill()
        for _ in range(4): # Par convention l'utilisation du _ comme itérateur pour indiquer une variable non utilisée
            turtle.forward(self.cote)
            turtle.right(90)
        turtle.end_fill()