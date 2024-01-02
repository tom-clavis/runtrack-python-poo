class Personne :
    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom
        
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
        
        
John = Personne("Doe", "John")
John.SePresenter()
print(John.SePresenter())

Jean = Personne("Dupont", "Jean")
Jean.SePresenter()
print(Jean.SePresenter())