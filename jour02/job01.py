class Rectangle:
    def __init__(self, longueur , largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        self.__longueur = longueur
    
    def set_largeur(self,largeur):
        self.__largeur = largeur
        
le_rectangle = Rectangle(10,5)

print("longueur initiale:", le_rectangle.get_longueur())
print("largeur initiale:", le_rectangle.get_largeur())

le_rectangle.set_longueur(12)
le_rectangle.set_largeur(6)

print("\nLongueur modifiée:", le_rectangle.get_longueur())
print("Largeur modifiée:", le_rectangle.get_largeur())