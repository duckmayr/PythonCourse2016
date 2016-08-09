def binarify(num):
	"""Convert positive integer to base 2"""
	if num <= 0: return '0'
	digits = []
	while num > 0:
		rem = str(num % 2)
		digits.insert(0,rem)
		num = num / 2
	return ''.join(digits)
	
def int_to_base(num, base):
	"""convert positive integer to a string in any base"""
	if num <= 0: return '0'
	digits = []
	while num > 0:
		rem = str(num % base)
		digits.insert(0,rem)
		num = num / base
	return ''.join(digits)
	
def base_to_int(string, base):
	"""take a string-formatted number and its base and return the base-10 integer"""
	if string=="0" or base <= 0 : return 0 
	result = 0
	for i in range(len(string)):
		result += base ** (len(string) - i - 1) * int(string[i])
	return result 
  
def flexibase_add(str1, str2, base1, base2):
	"""add two numbers of different bases and return the sum"""
	result = base_to_int(str1, base1) + base_to_int(str2, base2)
	return result

def flexibase_multiply(str1, str2, base1, base2):
	"""multiply two numbers of different bases and return the product"""
	result = base_to_int(str1, base1) * base_to_int(str2, base2)
	return result

def romanify(num):
	"""given an integer, return the Roman numeral version"""
	string = str(num)
	result = []
	for i in range(len(string)):
		if len(string) - i == 1:
			if int(string[i]) == 9:
				result.append("IX")
			elif int(string[i]) == 4:
				result.append("IV")
			elif int(string[i]) > 5:
				result.append("V" + "I" * (int(string[i]) - 5))
			elif int(string[i]) == 5:
				result.append("V")
			else:
				result.append("I" * int(string[i]))
		if len(string) - i == 2:
			if int(string[i]) == 9:
				result.append("XC")
			elif int(string[i]) == 4:
				result.append("XL")
			elif int(string[i]) > 5:
				result.append("L" + "X" * (int(string[i]) - 5))
			elif int(string[i]) == 5:
				result.append("L")
			else:
				result.append("X" * int(string[i]))
		if len(string) - i == 3:
			if int(string[i]) == 9:
				result.append("CM")
			elif int(string[i]) == 4:
				result.append("CD")
			elif int(string[i]) > 5:
				result.append("D" + "C" * (int(string[i]) - 5))
			elif int(string[i]) == 5:
				result.append("D")
			else:
				result.append("C" * int(string[i]))
		if len(string) - i == 4:
			result.append("M" * int(string[i]))
	result = ''.join(result)
	return result
	
