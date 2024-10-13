def menu():
    print("Kies een spel:")
    print("1: Galgje")
    print("2: Raad het Getal")
    print("3: Stop")

def spel():
    while True:
        menu()
        keuze = input("Typ 1, 2 of 3: ")

        if keuze == '1':
            from Opdracht_galgje import galgje_spel
            galgje_spel()
        elif keuze == '2':
            from nummer_raad_spel import raadhetgetal
            raadhetgetal()
        elif keuze == '3':
            print("Bedankt voor het spelen!")
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    spel()






