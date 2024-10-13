import random
import time

Galg = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|\\ |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========='''
]

woordenlijst = {
    "eenvoudig": ["huis", "fiets", "boom", "kat", "bal", "stoel", "tafel", "boek", "pen", "glas"],
    "gemiddeld": ["computer", "vogel", "afspraak", "winkel", "telefoon", "stoep", "school", "stoel", "lamp", "hond"],
    "moeilijk": ["maastricht", "bloemen", "klompen", "sinterklaas", "rijksmuseum", "afsluitdijk", "dijken",
                 "stroopwafel", "haring", "koningsdag"]
}

def weergeven_bord(woord, foute_gokken, goede_gokken):
    print(Galg[len(foute_gokken)])
    huidig_woord = ''.join(letter if letter in goede_gokken else '_' for letter in woord)
    print(f"Huidig woord: {huidig_woord}")

def tijd_gok(max_tijd):
    start_tijd = time.time()
    gok = input(f"Je hebt {max_tijd} seconden om een letter te raden: ").lower()
    verstreken_tijd = time.time() - start_tijd

    if verstreken_tijd > max_tijd:
        print(f"Te laat! Je hebt {verstreken_tijd:.2f} seconden genomen, niet te lang wachten!.")
        return None
    return gok

def galgje_spel():
    print("Welkom bij het spel Galgje!")

    moeilijkheid = input("Kies een moeilijkheidsgraad (eenvoudig/gemiddeld/moeilijk): ").lower()
    while moeilijkheid not in woordenlijst:
        moeilijkheid = input("Sorry dat kan niet. Kies een moeilijkheidsgraad (eenvoudig/gemiddeld/moeilijk): ").lower()

    gekozen_woord = random.choice(woordenlijst[moeilijkheid])
    foute_gokken = []
    goede_gokken = []
    max_tijd = 10

    while True:
        weergeven_bord(gekozen_woord, foute_gokken, goede_gokken)

        gok = tijd_gok(max_tijd)
        if gok is None:
            foute_gokken.append('?')
        else:
            if len(gok) != 1 or not gok.isalpha():
                print("Ongeldig, geef een enkele letter.")
                continue

            if gok in foute_gokken or gok in goede_gokken:
                print("Deze letter is al geraden. Probeer een andere.")
                continue

            if gok in gekozen_woord:
                goede_gokken.append(gok)
                if all(letter in goede_gokken for letter in gekozen_woord):
                    weergeven_bord(gekozen_woord, foute_gokken, goede_gokken)
                    print(f"Gefeliciteerd! Je hebt het woord '{gekozen_woord}' geraden!")
                    break
            else:
                foute_gokken.append(gok)
                if len(foute_gokken) >= 6:
                    weergeven_bord(gekozen_woord, foute_gokken, goede_gokken)
                    print(f"Jammer, je hebt het woord niet kunnen raden. Het juiste woord was '{gekozen_woord}'.")
                    break

if __name__ == "__main__":
    galgje_spel()
