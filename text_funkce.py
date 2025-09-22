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









