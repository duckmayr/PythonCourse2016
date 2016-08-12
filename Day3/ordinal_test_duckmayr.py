import unittest #You need this module
import my_ord #This is the script you want to test


class ordtest(unittest.TestCase):

	def test_first(self):
		ord_out=my_ord.ord(1)
		self.assertEqual('First', ord_out)
    
	def test_second(self):
		ord_out=my_ord.ord(2)
		self.assertEqual('Second', ord_out)
	
	def test_third(self):
		ord_out=my_ord.ord(3)
		self.assertEqual('Third', ord_out)
		
	def test_fourth(self):
		ord_out=my_ord.ord(4)
		self.assertEqual('Fourth', ord_out)
		
	def test_fifth(self):
		ord_out=my_ord.ord(5)
		self.assertEqual('Fifth', ord_out)
		
	def test_teens(self):
		ord_out=my_ord.ord(14)
		self.assertEqual('Fourteenth', ord_out)
		
	def test_twenties(self):
		ord_out=my_ord.ord(22)
		self.assertEqual('Twenty Second', ord_out)
		
	def test_notnumber(self):
		ord_out1=my_ord.ord('a')
		ord_out2=my_ord.ord(['a','b'])
		self.assertEqual('Put in a number.', ord_out1)
		self.assertEqual('Put in a number.', ord_out2)
		
if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()


