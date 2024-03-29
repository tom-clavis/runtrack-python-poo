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
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee=""):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")
        
personne1 = Personne()
eleve1 = Eleve()
prof = Professeur("Maths")

eleve1.afficherAge()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)


prof.modifierAge(40)
prof.bonjour()
prof.enseigner()
