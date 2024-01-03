class Livre:
    def __init__(self,titre,auteur,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
    
    def set_titre(self,titre):
        self.__titre = titre
        
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def set_pages(self,pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages n'est pas positif ou entier.")
            
mon_livre = Livre("Les Misérables", "Victor Hugo", 500)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_pages())

mon_livre.set_titre("Titeuf")
mon_livre.set_auteur("Zep")
mon_livre.set_pages(-40)  
mon_livre.set_pages(40)

print("\nTitre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_pages()) 