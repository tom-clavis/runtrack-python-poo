class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        return (f"{self.nom} - Numéro: {self.numero}, Position: {self.position}, "
                f"Buts: {self.buts_marques}, Passes: {self.passes_decisives}, "
                f"Jaunes: {self.cartons_jaunes}, Rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            print(joueur.afficher_statistiques())

    def mettre_a_jour_statistiques_joueur(self, nom_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges

equipe_om= Equipe("OM")
equipe_psg = Equipe("PSG")


joueur_a1 = Joueur("Deschamps", 10, "Attaquant")
joueur_a2 = Joueur("Ramos", 8, "Défenseur")
equipe_om.ajouter_joueur(joueur_a1)
equipe_om.ajouter_joueur(joueur_a2)

joueur_f1 = Joueur("Beckam", 10, "Milieu")
joueur_f2 = Joueur("Hazard", 1, "Gardien")
equipe_psg.ajouter_joueur(joueur_f1)
equipe_psg.ajouter_joueur(joueur_f2)

print("équipes avant la simulation:")
equipe_om.afficher_statistiques_joueurs()
equipe_psg.afficher_statistiques_joueurs()

joueur_a1.marquer_un_but()
joueur_a2.recevoir_un_carton_jaune()
joueur_f1.effectuer_une_passe_decisive()
joueur_f2.recevoir_un_carton_rouge()


equipe_om.afficher_statistiques_joueurs()
equipe_psg.afficher_statistiques_joueurs()