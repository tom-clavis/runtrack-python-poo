class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):  
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Vroum vroum ! La voiture démarre.")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Vroum vroum ! La moto démarre attention la Police .")


voiture_instance = Voiture("Honda", "CIVIC Type r", 2023, 70000)

voiture_instance.informationsVehicule()
voiture_instance.demarrer()

moto_instance = Moto("BWN", "GS 1250", 2021, 22500)

moto_instance.informationsVehicule()
moto_instance.demarrer()
