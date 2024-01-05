import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2

rectangle_instance = Rectangle(5, 3)

print(f"L'aire du Rectangle : {rectangle_instance.aire()}")

cercle_instance = Cercle(7)

print(f"L'aire du Cercle : {cercle_instance.aire()}")