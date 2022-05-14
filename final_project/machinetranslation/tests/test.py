import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), '') # Test for null input for frenchToEnglish
        self.assertEqual(english_to_french(''), '') # Test for null input for englishToFrench.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test for the translation of the world 'Hello'
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the world 'Bonjour'
unittest.main()