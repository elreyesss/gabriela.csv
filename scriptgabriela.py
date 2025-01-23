
import csv
import random
import string

def llegir_dades_csv(nom_arxiu):
    estudiantes = []
    with open(nom_arxiu, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            estudiantes.append(fila)

    return estudiantes

def generar_mail(nom, cognoms):
    
    email = f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ", "")
    return email

def generar_contrasenya(longitud=8):
    caracteres = string.ascii_letters + string.digits
    contrasenya = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasenya

def escriure_csv(estudiantes, nom_arxiu):
    with open(nom_arxiu, mode="w", encoding="utf-8", newline="") as f:
        fieldnames = estudiantes[0].keys()
        escritor = csv.DictWriter(f, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(estudiantes)
    print(f"Dades actualitzades al CSV: {nom_arxiu}")


# Exemple d'ús del programa
nom_arxiu_entrada = "estudiantes_nous.csv"
nom_arxiu_sortida = "estudiantes_actualitzats.csv"


# Llegir dades del CSV d'entrada
estudiantes = llegir_dades_csv(nom_arxiu_entrada)

# Afegir mail i contrasenya a cada estudiant
for estudiante in estudiantes:
    estudiante["mail"] = generar_mail(estudiante["nom"], estudiante["cognoms"])
    estudiante["contrasenya"] = generar_contrasenya()

# Escriure dades actualitzades al nou CSV
escriure_csv(estudiantes, nom_arxiu_sortida)

    