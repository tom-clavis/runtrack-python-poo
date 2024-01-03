class Voiture : 
    def __init__(self, marque, modele , année , kilometrage=0):
        self.__init__marque = marque
        self.__init__modele = modele 
        self.__init__année = année
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50 

    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def set_marque(self, marque):
        self.__marque = marque 
    
    def get_kilometrage(self):
        return self.__kilometrage 
    
    def get_en_marche(self):
        return self.__en_marche
    
    def get_reservoir(self):
        return self.__reservoir
    
    def set_modele(self, modele):
        self.__modele = modele 
    
    def set_annee(self, annee):
        self.__annee = annee 

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage 
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche 
    
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir 
    
    def __verifier_plein(self):
        return self.__reservoir > 5
    
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre vroum vroum.")
        else:
            print("La voiture ne peut pas démarrer, il manque de l'essence.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture a été arrêtée.")

voiture = Voiture("Honda", "CIVIC", 2023)



voiture.demarrer()  
print("État de la voiture en marche:", voiture.get_en_marche())

voiture.arreter()   
print("État de la voiture en marche:", voiture.get_en_marche())
