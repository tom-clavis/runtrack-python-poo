class Personne :
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
        
        
John = Personne("John", "Doe")
John.SePresenter()
print(John.SePresenter())

Jean = Personne("Jean", "Dupont")
Jean.SePresenter()
print(Jean.SePresenter())