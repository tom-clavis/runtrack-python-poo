class Livre:
    def __init__(self,titre,auteur,pages,):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
        
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
    
    def get_disponible(self):
        return self.__disponible
    
    def set_titre(self,titre):
        self.__titre = titre
        
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def set_pages(self,pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages n'est pas positif ou entier.")
            
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            print("Le livre est disponible. Emprunt en cours.")
            self.__disponible = False
        else:
            print("Le livre n'est plus disponible.")
            
    def rendre(self):
        if not self.verification():
            print("Le livre a bien été emprunté. Rendu en cours.")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")
            
mon_livre = Livre("Titeuf", "Zep", 40)

print("Le livre est disponible :", mon_livre.verification())

mon_livre.emprunter()

print("Le livre est disponible :", mon_livre.verification())

mon_livre.rendre()

print("Le livre est disponible :", mon_livre.verification())
