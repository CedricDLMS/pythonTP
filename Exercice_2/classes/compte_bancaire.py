from classes.client import Client
from datetime import datetime
import random
import string

class CompteBancaire():
    
    somme_totale_comptes : float = 0.0
    
    def __init__(self, date_creation_arg: str, client_arg, solde_arg: float):
        
        # Propriétés
        self.solde_client : float = solde_arg
        
        # Traitements sur la date
        try:
            self.date_creation = datetime.strptime(date_creation_arg, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La date doit être au format 'YYYY-MM-DD'.")
        
        
        # Traitement du client
        if not isinstance(client_arg, Client):
            raise ValueError("Le client doit être une instance de la classe Client.")
        else:
            self.client = client_arg

        # Génération de l'identifiant unique
        self.__identifiant_interne = self.__generer_identifiant()
        
        #ajout aux comptes :
        CompteBancaire.somme_totale_comptes += self.solde_client
    
    def ajouter_argent(self,montant_ajouter_arg : float) :
        if not isinstance(montant_ajouter_arg, float):
            raise ValueError("Le montant doit etre un nombre")
        else:
            self.solde_client += montant_ajouter_arg
    
    
    #Methode privée pour génerer identifiant unique
    def __generer_identifiant(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=4))
        date_str = self.date_creation.strftime("%d%m%Y")
        return f"{lettres}{date_str}"
    
    @property
    def identitfiant_interne(self):
        return self.__identifiant_interne
    
    @staticmethod
    def total_soldes():
        return CompteBancaire.somme_totale_comptes
    
    def __str__(self) -> str:
        return f"Le compte de {self.client.nom} {self.client.prenom} a été crée le {self.date_creation} avec ID : {self.identitfiant_interne}"
    
    def __eq__(self, other):
        if not isinstance(other, CompteBancaire):
            return False
        return self.solde_client == other.solde_client
    
        