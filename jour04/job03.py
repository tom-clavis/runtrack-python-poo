class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        if longueur > 0:
            self.__longueur = longueur
        else:
            print("La longueur doit être positive.")

    def set_largeur(self, largeur):
        if largeur > 0:
            self.__largeur = largeur
        else:
            print("La largeur doit être positive.")


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        if hauteur > 0:
            self.__hauteur = hauteur
        else:
            print("La hauteur doit être positive.")

    def volume(self):
        
        return self.get_longueur() * self.get_largeur() * self.__hauteur

rectangle_instance = Rectangle(5, 3)

print(f"Longueur du rectangle : {rectangle_instance.get_longueur()}")
print(f"Largeur du rectangle : {rectangle_instance.get_largeur()}")
print(f"Périmètre du rectangle : {rectangle_instance.perimetre()}")
print(f"Surface du rectangle : {rectangle_instance.surface()}")

rectangle_instance.set_longueur(7)
rectangle_instance.set_largeur(4)

print(f"Nouvelle longueur du rectangle : {rectangle_instance.get_longueur()}")
print(f"Nouvelle largeur du rectangle : {rectangle_instance.get_largeur()}")
print(f"Nouveau périmètre du rectangle : {rectangle_instance.perimetre()}")
print(f"Nouvelle surface du rectangle : {rectangle_instance.surface()}")

parallelepipede_instance = Parallelepipede(5, 3, 2)

print(f"Hauteur du parallélépipède : {parallelepipede_instance.get_hauteur()}")
print(f"Volume du parallélépipède : {parallelepipede_instance.volume()}")
