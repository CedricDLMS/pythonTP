from classes.entreprise import Entreprise


if __name__ == "__main__":
    
    try :
        
        entreprise = Entreprise("DigiVie", "123 Rue vies, 34000 Montpellier", "12345678123455")
        
        print(entreprise)
        
        entreprise.siret = 123456789e1111
        
        print(entreprise)
        
    except Exception as e:
        print(e)