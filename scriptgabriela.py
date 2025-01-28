import csv 
import random 
import string 

def llegir_dades_csv(nom_fitxer): 
    estudiants = [] 
    with open(nom_fitxer, mode='r', encoding='utf-8') as fitxer: 
        lector = csv.DictReader(fitxer) 
        for fila in lector:  
            estudiants.append(fila)
    return estudiants
   
def genenrar_mail(nom, cognoms):
    email = f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ", "")
    return email

def generar_contrasenya(): 
    caracters = string.ascii_letters + string.digits + string.punctuation
    contrasenya = ''.join(random.choice(caracters) for i in range(10))

    return contrasenya

def escriure_csv(estudiants, nom_arxiu):
    with open(nom_arxiu, mode='w', newline='', encoding='utf-8') as fitxer:
        camps = list(estudiants[0].keys()) + ['email', 'contrasenya']
        escriptor = csv.DictWriter(fitxer, fieldnames=camps)
        escriptor.writeheader()
        for estudiant in estudiants:
            estudiant['email'] = genenrar_mail(estudiant['nom'], estudiant['cognoms'])
            estudiant['contrasenya'] = generar_contrasenya()
            escriptor.writerow(estudiant)
            
# EXEMPLE D'US DEL PROGRAMA
nom_arxiu_entrada ='estudiants_nous.csv'
estudiants = llegir_dades_csv(nom_arxiu_entrada)
for estudiant in estudiants: 
    estudiant['email'] = genenrar_mail(estudiant['nom'], estudiant['cognoms'])
    estudiant['contrasenya'] = generar_contrasenya()

nom_arxiu_sortida = 'alta_nous_estudiants.csv'
escriure_csv(estudiants, nom_arxiu_sortida)
print(f"Fitxer {nom_arxiu_sortida} generat correctament")
print(estudiants)