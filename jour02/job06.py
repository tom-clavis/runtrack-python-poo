class Commande : 
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {} 
        self.__statut = "en cours" 
        self.__total = 0  
        
    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {'prix': prix, 'quantite': 1}
        else:
            self.__plats_commandes[nom_plat]['quantite'] += 1
        self.__total += prix
        print(f"Plat {nom_plat} ajouté avec succès.")

    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__total = 0
        self.__statut = "annulée"
        print("La commande a été annulée.")

    