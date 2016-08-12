import unittest #You need this module
from lab3_duckmayr import * #This is the script you want to test


class mytest(unittest.TestCase):

	def test_shout(self):
		self.assertEqual("I NEED A TOURNIQUET!", shout("I need a tourniquet."))
		self.assertEqual("I NEED A TOURNIQUET!", shout("I need a tourniquet?"))
		self.assertEqual("I NEED A TOURNIQUET!", shout("I need a tourniquet"))
		self.assertEqual("I NEED A TOURNIQUET!", shout("I NEED A TOURNIQUET!"))
    
	def test_reverse(self):
		self.assertEqual('nA', reverse('An'))
		self.assertEqual('...secnetnes tset esoht ta kool a ekaT !woW', reverse('Wow! Take a look at those test sentences...'))
		
	def test_reversewords(self):
		self.assertNotEqual('nA', reversewords('An'))
		self.assertNotEqual('...secnetnes tset esoht ta kool a ekaT !woW', reversewords('Wow! Take a look at those test sentences...'))
		self.assertEqual("sentences... test those at look a Take Wow!", reversewords('Wow! Take a look at those test sentences...'))
		
	def test_reversewordletters(self):
		self.assertEqual('nA', reversewordletters('An'))
		self.assertEqual('!woW ekaT a kool ta esoht tset ...secnetnes', reversewordletters('Wow! Take a look at those test sentences...'))
		self.assertNotEqual("sentences... test those at look a Take Wow!", reversewordletters('Wow! Take a look at those test sentences...'))
		
	def test_piglatin(self):
		self.assertEqual("oogle-Gay", piglatin('Google'))
		self.assertEqual("An-ay", piglatin('An'))
		self.assertEqual('ow-Hay o-day ou-yay ut-pay a-ay entence-say into-ay iglatin-pay', piglatin('How do you put a sentence into piglatin'))
		self.assertNotEqual("Google-ay", piglatin('Google'))
		self.assertNotEqual("n-Aay", piglatin('An'))
		self.assertNotEqual("Google", piglatin('Google'))
	
	def test_NoTextException(self):
		with self.assertRaises(NoTextException):
			piglatin(1234)

if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()


