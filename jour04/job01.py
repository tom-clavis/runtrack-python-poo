class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(f"Il possède  : {self.age} années")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):
    def __init__(self):
        super().__init__()
        
    def allerEnCours(self):
        print("Je vais en cours (j'ai trop la flemme)")

    def afficherAge(self):
        print(f"J'ai {self.age} ans et toute mes dents")
        
class Professeur:
    def __init__(self, matiereEnseignee=""):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")
        
personne1 = Personne()
eleve1 = Eleve()

eleve1.afficherAge()