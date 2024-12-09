import csv

#variables necessaires aux calculs

ages : float = []
total_classe_1 : int = 0
total_classe_2 : int = 0
total_classe_3 : int = 0
survivant_classe_1 : int = 0
survivant_classe_2 : int = 0
survivant_classe_3 : int = 0
bateau = dict()

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
        

poucentage_survivant_1 = (survivant_classe_1 / total_classe_1) * 100
poucentage_survivant_2 = (survivant_classe_2 / total_classe_2) * 100
poucentage_survivant_3 = (survivant_classe_3 / total_classe_3) * 100

print(poucentage_survivant_1)
print(poucentage_survivant_2)
print(poucentage_survivant_3)