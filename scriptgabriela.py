import csv
import random
import string

def llegir_dades_csv(nom_archivo):
    estudiantes = []
    with open(nom_archivo,mode="r",encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            estudiantes.append(fila)

    return estudiantes

def generar_mail(nom,cognoms):
    email=f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ","")
    print(email)

def generar_contrasenya():
    caracteres = string.ascii_letters + string.digits
    contrasenya = "".join(random.choice(caracteres))
    return contrasenya

def escriure_csv(estudiante,nom_archivo):
    print(estudiante)

#EXEMPLE D'US DEL PROGRAMA

nom_arxiu_entrada="estudiantes_nous.csv"
estudiantes=llegir_dades_csv(nom_arxiu_entrada)

for estudiante in "estudiantes":
    estudiante["mail"] = generar_mail(estudiante["nom"],estudiante["cognoms"])
    estudiante["contrasenya"] = generar_contrasenya()

    