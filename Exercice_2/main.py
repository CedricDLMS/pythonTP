from classes.client import Client
from classes.compte_bancaire import CompteBancaire


if __name__ == "__main__" :
    
    # Création d'un client
    client1 = Client("Dupont", "Jean", "123 Rue Exemple, Paris", "123456789012345")

    # Création de deux comptes bancaires
    compte1 = CompteBancaire("2024-12-01", client1, 1000.0)
    compte2 = CompteBancaire("2024-12-05", client1, 1500.0)

    # Affichage des comptes
    print(compte1)
    print(compte2)

    # Affichage des identifiants internes
    print(compte1.identitfiant_interne)
    print(compte2.identitfiant_interne)

    # Comparaison des comptes
    print(compte1 == compte2)

    # Somme totale des soldes
    print(f"Somme totale des soldes: {CompteBancaire.total_soldes():.2f} €")


 