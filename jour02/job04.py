class Student:
    def __init__(self, nom, prenom, idetudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__idetudiant = idetudiant
        self.__credits = credits
        self.__level = "Insuffisant"
        
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            print(f"{credits} ajout de crédits")
            self.__studentEval()
            
    def __studentEval(self):
        if self.__credits >= 90:
            self.__level = "Excellent"
        elif self.__credits >= 80:
            self.__level = "Très bien"
        elif self.__credits >= 70:
            self.__level = "Bien"
        elif self.__credits >= 60:
            self.__level = "Passable"
        else:
            self.__level = "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom : {self.__nom}")
        print(f"prenom : {self.__prenom}")
        print(f"id : {self.__idetudiant}")
        print(f"Level : {self.__level}")
        

Luc_Van = Student(prenom="Luc", nom="Van", idetudiant=145)

Luc_Van.add_credits(0)
Luc_Van.studentInfo()

Luc_Van.add_credits(60)
Luc_Van.studentInfo()

Luc_Van.add_credits(20)
Luc_Van.studentInfo()

Luc_Van.add_credits(10)
Luc_Van.studentInfo()

Luc_Van.add_credits(10)
Luc_Van.studentInfo()