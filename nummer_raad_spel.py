import random

def raadhetgetal():
    print("Welkom bij het spel RaadHetGetal")
    pogingen = int(input("Hoeveel gokken wil je krijgen?: "))
    min_val = int(input("Wat is de minimale hoogte van je geheime cijfer?: "))
    max_val = int(input("Wat is de maximale hoogte van je geheime cijfer?: "))

    geheim_getal = random.randint(min_val, max_val)

    print(f"Je hebt {pogingen} pogingen om het getal tussen {min_val} en {max_val} te raden.")

    for poging in range(pogingen):
        gok = int(input(f"Poging {poging + 1}: Voer je gok in: "))

        if gok < geheim_getal:
            print("Het getal is groter dan je gok.")
        elif gok > geheim_getal:
            print("Het getal is kleiner dan je gok.")
        else:
            print(f"Goed gedaan! Je hebt het getal {geheim_getal} geraden.")
            break
    else:
        print(f"Helaas :(. Het juiste getal was {geheim_getal}.")

if __name__ == "__main__":
    raadhetgetal()








