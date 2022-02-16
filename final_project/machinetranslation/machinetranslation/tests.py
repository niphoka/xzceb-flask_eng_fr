import unittest
from translator import french_to_english
from translator import english_to_french

class TestMyModule(unittest.TestCase):
	def f2e1(self):
		self.assertEqual(french_to_english(('Bonjour, comment vous'),('Hello, how are')))
	def f2e2(self):
		self.assertEqual(french_to_english(('Bonjour'), ('Hello')))
	def f2e3(self):
		self.assertEqual(french_to_english('None'), '')
	def f2e4(self):
		self.assertEqual(french_to_english(0), 0)
		
# This is Nixon's work


class TestMyModule1(unittest.TestCase):
	def e2f1(self):
		self.assertEqual(english_to_french(('Hello, how are'), ('Bonjour, comment vous')))
	def e2f2(self):
		self.assertEqual(english_to_french(('Hello'), ('Bonjour')))
	def e2f3(self):
		self.assertEqual(english_to_french('None'), "")
	def e2f4(self):
		self.assertEqual(english_to_french(0), 0)

unittest.main()