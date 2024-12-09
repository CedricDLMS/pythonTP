class Client():
    def __init__(self, nom_arg: str, prenom_arg: str, adresse_arg: str, nir_arg: str):
        self.nom = nom_arg
        self.prenom = prenom_arg
        self.adresse = adresse_arg
        
        if len(str(nir_arg)) != 15:
            raise ValueError("Le numéro de sécurité sociale (NIR) doit être composé de 15 chiffres.")
        elif not nir_arg.isdigit():
            raise ValueError("Le numéro de sécurité sociale (NIR) doit être composé de chiffres uniquement.")
        else:
            self.__nir = nir_arg

    # Getter pour le NIR
    @property
    def nir(self):
        return self.__nir

    # Setter pour le NIR
    @nir.setter
    def nir(self, nir_arg):
        if len(str(nir_arg)) != 15:
            raise ValueError("Le numéro de sécurité sociale (NIR) doit être composé de 15 chiffres.")
        elif not nir_arg.isdigit():
            raise ValueError("Le numéro de sécurité sociale (NIR) doit être composé de chiffres uniquement.")
        else:
            self.__nir = nir_arg

    def __str__(self):
        return f"Client {self.prenom} {self.nom}, résidant au {self.adresse}, possède le NIR {self.nir}."
