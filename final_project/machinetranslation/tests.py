import unittest

from translator import french_to_english , english_to_french

class Test(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english(None), "")
    def test2(self):
        self.assertNotEqual(english_to_french(None),"")
    def test3(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test4(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__=="__main__":
    unittest.main()