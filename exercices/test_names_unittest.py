import unittest

MIN_LENGTH = 7

def names(prenoms: list[str]) -> int:
    return sum(1 for prenom in prenoms if len(prenom) > MIN_LENGTH)

class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(names(prenoms), 4)

if __name__ == "__main__":
    unittest.main()