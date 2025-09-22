from text_funkce import to_lower, delka_textu, spocitej_slova, vrat_suda, pocet_pismen_bez_mezer, vyber_velka_slova

def test_to_lower():
    assert to_lower("Ahoj") == "ahoj"
    assert to_lower("AHOJ") == "ahoj"

def test_delka_textu():
    assert delka_textu("text") == 4
    assert delka_textu("") == 0

def test_spocitej_slova():
    assert spocitej_slova("Ahoj jak se máš") == 4
    assert spocitej_slova("") == 0

def test_vrat_suda():
    assert vrat_suda("Ahoj jak je") == ['Ahoj', 'je']
    assert vrat_suda("Dobrý den") == []

def test_pocet_pismen_bez_mezer():
    assert pocet_pismen_bez_mezer("a b c d ") == 4
    assert pocet_pismen_bez_mezer("  ") == 0
    assert pocet_pismen_bez_mezer("") == 0
    assert pocet_pismen_bez_mezer(" A b Č") == 3

def test_vyber_velka_slova():
    assert vyber_velka_slova("Ahoj jak se máš", 3) == ['Ahoj', 'jak', 'máš']
    assert vyber_velka_slova("", 2) == []
    assert vyber_velka_slova("Ahoj jak se máš", 10) == []

