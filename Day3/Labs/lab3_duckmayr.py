import string
import traceback

class NoTextException(Exception):
	def __init__(self):
		Exception.__init__(self, "You need to put in text if you want to convert text!")

def shout(txt):
	if txt[-1] in ['.','?',','';']: txt = txt[:-1]
	if txt[-1] != "!": txt += "!"
	return txt.upper()

def reverse(txt):
	return txt[::-1]
  
def reversewords(txt):
	return ' '.join(txt.split()[::-1])

def reversewordletters(txt):
	return reverse(reversewords(txt))
  
def piglatin(txt):
	if type(txt) != str: raise NoTextException
	txt = txt.split()
	for block in range(len(txt)):
		if txt[block][0].lower() in ['a','e','i','o','u']: txt[block] += '-ay'
		else: txt[block] = txt[block][1:] + '-' + txt[block][0] + 'ay'
	return ' '.join(txt)