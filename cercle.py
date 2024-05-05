from forme import Forme
import turtle

class Cercle(Forme):
    def __init__(self, rayon, couleur):
        super().__init__(couleur)
        self.rayon = rayon

    def dessiner(self):
        turtle.color(self.couleur)
        turtle.begin_fill()
        turtle.circle(self.rayon)
        turtle.end_fill()