import csv

#variables necessaires aux calculs

ages : float = []
total_classe_1 : int = 0
total_classe_2 : int = 0
total_classe_3 : int = 0
survivant_classe_1 : int = 0
survivant_classe_2 : int = 0
survivant_classe_3 : int = 0
bateau = {}

with open('./annexes/titanic_survival.csv', encoding='utf-8') as csvfiles:
    reader = csv.DictReader(csvfiles, delimiter=',')
    next(reader)
    
    for row in reader:
        age = row['age']
        if age and age.strip():  # Vérifie que la cellule n'est pas vide
            try:
                ages.append(float(age))
            except ValueError:
                pass  # Ignore les âges invalides
        
        try:
            survived = int(row['survived'])
            pclass = int(row['pclass'])
            
            
            if pclass == 1:
                total_classe_1 += 1
                if survived == 1:
                    survivant_classe_1 += 1
            elif pclass == 2:
                total_classe_2 += 1
                if survived == 1:
                    survivant_classe_2 += 1
            elif pclass == 3:
                total_classe_3 += 1
                if survived == 1:
                    survivant_classe_3 += 1
        except:
            pass
        
        try :
            bateau_row = int(row['boat'])
            if bateau_row not in bateau:
                bateau[bateau_row] = 1
            else :
                bateau[bateau_row] += 1
        except:
            pass
        

poucentage_survivant_1 = (survivant_classe_1 / total_classe_1) * 100
poucentage_survivant_2 = (survivant_classe_2 / total_classe_2) * 100
poucentage_survivant_3 = (survivant_classe_3 / total_classe_3) * 100

bateau_max = max(bateau, key=bateau.get) #variables pour le bateau le plus performant 
valeur_max = bateau[bateau_max]

print("------------------------------------------------------------------------")
print("---------------------------MOYENNE D'AGE--------------------------------")
print("------------------------------------------------------------------------")

moyenne_age = sum(ages) / len(ages)

print(f"La moyenne d'age est : {moyenne_age:.2f}")

print("------------------------------------------------------------------------")
print("-----------------------POURCENTAGE DE SURVIE----------------------------")
print("------------------------------------------------------------------------")

print(f"Pourcentage de survivants en classe 1 : {poucentage_survivant_1:.2f}%")
print(f"Pourcentage de survivants en classe 2 : {poucentage_survivant_2:.2f}%")
print(f"Pourcentage de survivants en classe 3 : {poucentage_survivant_3:.2f}%")



print("------------------------------------------------------------------------")
print("-------------------------BATEAUX SAUVETEURS-----------------------------")
print("------------------------------------------------------------------------")

for cle,valeur in bateau.items():
    print(f"dans le bateau : {cle} , nous avons {valeur} survivants")

print("------------------------------------------------------------------------")
print("-------------------------BATEAU LE PLUS GENIAL--------------------------")
print("------------------------------------------------------------------------")
print(f"Le bateau avec le plus de survivants est le bateau {bateau_max}, avec {valeur_max} survivants.")
