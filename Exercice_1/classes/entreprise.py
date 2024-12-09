class Entreprise() :
    def __init__(self, nom_arg : str, adresse_arg : str, siret_arg) :
        self.nom = nom_arg
        self.adresse = adresse_arg
        
        if len(str(siret_arg)) != 14 :
            raise ValueError("Le numero de siret doit être composé de 14 chiffres")
        elif not siret_arg.isdigit() :
            raise ValueError("Le numero de siret doit être composé de chiffres uniquement")
        else:
            self.__siret = siret_arg
        
    # Getter pour le siret
    @property
    def siret(self):
        return self.__siret
    
    # Setter pour le nom
    @siret.setter
    def siret(self, siret_arg):
        if len(str(siret_arg)) != 14 :
            raise ValueError("Le numero de siret doit être composé de 14 chiffres")
        elif not siret_arg.isdigit() :
            raise ValueError("Le numero de siret doit être composé de chiffres uniquement")
        else:
            self.__siret = siret_arg
            
    def __str__(self):
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET {self.siret}."