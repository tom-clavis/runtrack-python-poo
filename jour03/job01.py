class Ville:
    def __init__(self, nom, nombre_habitants):
        self.nom = nom
        self._nombre_habitants = nombre_habitants  
    
    def get_nom(self):
        return self.__nom
        
    def get_nombre_habitants(self):
        return self._nombre_habitants

    def ajouter_population(self, nombre=1):
        self._nombre_habitants += nombre


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville

    def ajouter_population(self):
        self.__ville.ajouter_population()



ville_paris = Ville("Paris la ville de merde", 1000000)
ville_marseille = Ville("Marseille", 861635)


print(f"Population de la ville de : {ville_paris.nom}: {ville_paris.get_nombre_habitants()}")
print(f"Population de la ville de : {ville_marseille.nom}: {ville_marseille.get_nombre_habitants()}")


john = Personne("John", 45, ville_paris)
myrtille = Personne("Fraise Framboise Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)


john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()


print(f"Mise à jour de  {ville_paris.nom} : {ville_paris.get_nombre_habitants()}")
print(f"Mise à jour de  {ville_marseille.nom} : {ville_marseille.get_nombre_habitants()}")