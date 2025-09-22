import unittest
from text_funkce import to_lower, delka_textu, spocitej_slova, vrat_suda, pocet_pismen_bez_mezer, vyber_velka_slova


class TestTextFunkce(unittest.TestCase):

    def test_to_lower(self):
        # Testujeme převod na malá písmena
        self.assertEqual(to_lower("Ahoj"), "ahoj")
        self.assertEqual(to_lower("TEST"), "test")
        self.assertEqual(to_lower("Python"), "python")

    def test_delka_textu(self):
        # Testujeme délku textu
        self.assertEqual(delka_textu("text"), 4)
        self.assertEqual(delka_textu(""), 0)
        self.assertEqual(delka_textu("ahoj svete"), 10)

    def test_spocitej_slova(self):
        self.assertEqual(spocitej_slova("Ahoj jak se máš"),4)
        self.assertEqual(spocitej_slova(""),0)

    def test_vrat_suda(self):
        self.assertEqual(vrat_suda("Ahoj jak je"),["Ahoj", "je"])
        self.assertEqual(vrat_suda("Dobrý den"),[])

    def test_pocet_pismen_bez_mezer(self):
        self.assertEqual(pocet_pismen_bez_mezer("a b c d "),4)
        self.assertEqual(pocet_pismen_bez_mezer("A B c d "),4)
        self.assertEqual(pocet_pismen_bez_mezer("a b č Ř "),4)
        self.assertEqual(pocet_pismen_bez_mezer(""),0)
        self.assertEqual(pocet_pismen_bez_mezer("     "),0)
        self.assertEqual(pocet_pismen_bez_mezer("abc"),3)

    def test_vyber_velka_slova(self):
        self.assertEqual(vyber_velka_slova("Ahoj jak se máš", 3),["Ahoj", "jak", "máš"])



if __name__ == "__main__":
    unittest.main()
