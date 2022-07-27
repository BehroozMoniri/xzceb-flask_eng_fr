import unittest

from translator import french_to_english , english_to_french

class Test(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english(None), None )
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french(None),None)
    def test_english_to_french_(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test_french_to_english_(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__=="__main__":
    unittest.main()
