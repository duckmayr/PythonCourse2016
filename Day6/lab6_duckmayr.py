#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

#Exercise 2
#Write a function that returns prime numbers less than 121

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



# Exercise 1

def getGCF(num1, num2, n = 0):
	if n == 0: n = min(num1, num2)
	if num1 % n == 0 and num2 % n == 0: return n
	return getGCF(num1, num2, n-1)

# Exercise 2
	
def getPrimes(highest = 121):
	if highest < 2: return None
	if highest == 2: return [2]
	for i in range(2, highest):
		if highest % i == 0: return getPrimes(highest - 1)
	return getPrimes(highest - 1) + [highest]
	
# Exercise 3
	
