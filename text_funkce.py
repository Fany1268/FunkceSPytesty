from os.path import split


def to_lower(text):
    vstup = text.lower()
    return vstup

# vysledek = to_lower(input("Napiš text: "))
# print(vysledek)

def delka_textu(text):
    """
spočítá délku textu
    :param text: string
    :return: int
    """
    vystup = len(text)   # použijeme vestavěnou funkci len()
    return vystup

# vysledek = delka_textu(input("Napiš text: "))
# print(vysledek)

def spocitej_slova(text):
    """
spočítá počet slov v textu
    :param text: string
    :return: int
    """
    rozdeleni = text.split()
    delka = len(rozdeleni)
    vystup = delka
    return vystup

# vysledek = spocitej_slova(input("Napiš text: "))
# print(vysledek)

def vrat_suda(text):
    """
vrátí slova ze sudým počtem písmen
    :param text: string
    :return: list
    """
    suda = []
    slova = text.split()
    for slovo in slova:
     if len(slovo) % 2 == 0:
      suda.append(slovo)
    return suda

# vysledek = vrat_suda(input("Napiš text: "))
# print(vysledek)

def pocet_pismen_bez_mezer(text):
    pocet = 0
    znak = []
    for znak in text:
        if znak != " ":
         pocet += 1
    return pocet

# vysledek = pocet_pismen_bez_mezer(input("Napiš text: "))
# print(vysledek)

def vyber_velka_slova(text, min_delka_slova):
    """

    :param text: string
    :param min_delka_slova: int
    :return: list
    """
    vysledek = []
    slova = text.split()

    for slovo in slova:
        if len(slovo) >= min_delka_slova:
            vysledek.append(slovo)
    return vysledek

# vypocet = vyber_velka_slova("Napiš slova a dddddddd hhhhhhghgh", 2 )
# print(vypocet)

# text = input("Napiš text: ")
# min_delka_slova = int(input("Napiš číslo: "))
# vypis = vyber_velka_slova(text, min_delka_slova)
# print(vypis)

def nejdelsi_slovo(text):
    """
vrací nejdelší slovo
    :param text: string
    :return: string
    """
    nejdelsi = ""
    slova = text.split()
    for slovo in slova:
        if len(slovo) > len(nejdelsi):
            nejdelsi = slovo
        else:continue
    return (f"Nejdelší slovo je: {nejdelsi} a má {len(nejdelsi)} znaky")  # tuple s f string: (slovo, délka)
    # return (nejdelsi, len(nejdelsi))  # tuple: (slovo, délka)

# vysledek = input("Napiš slova")
# print(nejdelsi_slovo(vysledek))


def nejmensi_cislo(cisla):
    """
vtací nejmenší číslo
    :param cisla: list
    :return: int
    """
    # hláška ne do konzole ale pro programátora chybového hlášení
    if not cisla:
        raise ValueError("Seznam nesmí být prázdný.")
    nej = cisla[0]            # začneme prvním číslem v seznamu
    for cislo in cisla:       # projdeme všechna čísla
        if cislo < nej:       # pokud je aktuální menší než dosavadní minimum
            nej = cislo       # aktualizujeme nejmenší číslo
    return nej                # vrátíme výsledek

tisk = nejmensi_cislo([2, 3, 4])
print(tisk)







