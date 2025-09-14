# opretter liste
snapse=[]
# Funktion til oprettelse af snaps og snapseejer
antal_spillere=int(input("hvor mange spillere er I?"))

for i in range(antal_spillere):
    navn=input("Skriv dit navn")
    snapsenavn=input("Skriv navnet på din snaps")
    snapse.append({"navn":navn,"snapsenavn":snapsenavn})
    print(snapse)


# Funktion til at skrive til CSV fil
with open("snapse.txt","w") as f:
    f.write()

# Funktion til bedømmelse af snaps

# Funktion til dashboard af snaps - og kunne se vinder

