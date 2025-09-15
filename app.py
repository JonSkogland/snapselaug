# requirements
import csv
import pandas as pd

# opretter liste
snapse = []
# Funktion til oprettelse af snaps og snapseejer
antal_spillere=int(input("hvor mange spillere er I?: "))

for i in range(antal_spillere):
    navn = input("Skriv dit navn: ")
    snapsenavn = input("Skriv navnet på din snaps: ")
    snapse.append({"navn": navn, "snapsenavn": snapsenavn})


# Funktion til at skrive til CSV fil
with open("snapse.csv", "w", newline="", encoding="utf-8") as csvfile:
    key_navne = snapse[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=key_navne)
    writer.writeheader()
    writer.writerows(snapse)

# Funktion til bedømmelse af snaps

# Funktion til dashboard af snaps - og kunne se vinder

def læs_csvfil():
    # Initialisere liste til gem af data
    indlæst_data = []

    # Læs fil
    with open("snapse.csv", newline="") as csvfile:
        snapselæser = csv.DictReader(csvfile, fieldnames=("navn", "snapsenavn"))
        next(snapselæser) # Skipper første række af snapselæser, da der er kolonnenavne i.

        # Indlæs rækker til dictionary
        for row in snapselæser:
            indlæst_data.append(row) # Tilføj dict til listen

    return indlæst_data
        

print(læs_csvfil())



