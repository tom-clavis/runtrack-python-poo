class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
rectangle_instance = Rectangle(5, 3)

print(f"Aire du rectangle : {rectangle_instance.aire()}")