import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1] 
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']  
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_total(self, main):
        total = sum(carte.valeur for carte in main)
        as_present = any(carte.valeur == 1 for carte in main)
        if as_present and total + 10 <= 21:
            return total + 10
        return total

    def afficher_main(self, main):
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer(self):
        joueur_main = [self.paquet.pop(), self.paquet.pop()]  
        croupier_main = [self.paquet.pop(), self.paquet.pop()]  

        while True:
            print("\nMain du joueur :")
            self.afficher_main(joueur_main)
            total_joueur = self.calculer_total(joueur_main)
            print(f"Total : {total_joueur}")

            if total_joueur == 21:
                print("Blackjack ! Le joueur gagne.")
                break
            elif total_joueur > 21:
                print("Le joueur a dépassé 21. Le croupier gagne.")
                break

            choix = input(" Le Croupier demande : Carte ? (Oui/Non): ").lower()
            if choix == 'oui':
                joueur_main.append(self.paquet.pop())
            else:
                break

        while self.calculer_total(croupier_main) < 17:
            croupier_main.append(self.paquet.pop())

        print("\nMain du croupier :")
        self.afficher_main(croupier_main)
        total_croupier = self.calculer_total(croupier_main)
        print(f"Total : {total_croupier}")

        if total_croupier > 21:
            print("Le croupier a dépassé 21. Le joueur gagne.")
        elif total_joueur > total_croupier:
            print("Le joueur gagne, bravo vous êtes riche !")
        elif total_joueur < total_croupier:
            print("Le croupier gagne, bravo retour à pôle emplois.")
        else:
            print("Égalité.")


jeu_blackjack = Jeu()
jeu_blackjack.jouer()
