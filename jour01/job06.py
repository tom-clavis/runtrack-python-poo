class Animal : 
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nouveau_prenom):
        self.prenom = nouveau_prenom 
        
        
animal = Animal()
print(f"L'âge de l'animal : {animal.age} ans.")

animal.vieillir()
print(f"L'âge de l'animal : {animal.age} ans")

animal.nommer("Luc Van Der Meijden")
print(f"L'animal s'appel {animal.prenom}")