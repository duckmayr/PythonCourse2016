def ord(ord_in):
	"""This is a function that converts integers, or floats that can be converted to integers, to ordinal string representation."""
	try:
		ord_in = int(ord_in)
	except:
		return 'Put in an integer.'
	else:
		use_for_ones = {1:'First', 2:'Second', 3:'Third', 4:'Fourth', 5:'Fifth', 6:'Sixth', 7:'Seventh', 8:'Eighth', 9: 'Ninth'}
		use_for_teens = {11:'Eleventh', 12:'Twelfth', 13: 'Thirteenth', 14:'Fourteenth', 15:'Fifteenth', 16:'Sixteenth', 17:'Seventeenth', 18: 'Eighteenth', 19:'Nineteenth'}
		use_for_zeroes = {10:'Tenth', 20: 'Twentienth', 30:'Thirtieth', 40: 'Fortieth', 50:'Fiftieth', 60:'Sixtieth', 70: 'Sixtieth', 80}
		use_for_others = {2:}
		ones = int(str(ord_in)[-1])
		if len(str(ord_in)) > 1:
			tens = int(str(ord_in)[-2])
		if len(str(ord_in)) > 2:
			hundreds = int(str(ord_in)[-3])
		ord_out = []
		if hundreds:
			ord_out.append()
			
### I eventually abandoned this because Dave showed my I was doing it wrong and we moved on to the lab.