class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte}: {self.__nom} {self.__prenom}")

    def afficher_solde(self):
        print(f"Solde du compte {self.__numero_compte}: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Opération impossible. Solde insuffisant.")

compte1 = CompteBancaire(1, "Damien", "Damien", 1000)
compte2 = CompteBancaire(2, "Cordial", "Alicia", -500, decouvert=True)

compte1.afficher()
compte1.afficher_solde()

compte2.afficher()
compte2.afficher_solde()

compte1.versement(500)
compte1.retrait(200)

compte2.agios(0.02)

compte1.virement(compte2, 600)

compte1.afficher_solde()
compte2.afficher_solde()
