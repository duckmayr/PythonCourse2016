"""This script introduces the Portfolio class, the Investment class, and the
Stock and MutualFund subclasses of the Investment class to allow the user to
keep track of transactions for one or more investment portfolios. Importing
the module also creates the global objects 'market', a dictionary of several 
lists and dictionaries used to keep track of all existing Investment objects,
and 'portfolios', a list of all existing Portfolio objects. See the help for
each object class or the functions 'unDict', 'strToFund', 'notFund', 'putDate'
'putTime', 'timeStamp', or 'printMarket' for more information."""

from random import * # This allows for randomly determined selling prices
from datetime import *	# This enables a time stamp for the audit log

market = {'stocks':[],'mutualFunds':[],'symbols':{},'funds':{}}

portfolios = []

def unDict(fund_in):
	"""Returns a string of the shares of an Investment type in a Portfolio"""
	return ', '.join([str(v)+' shares of '+str(k) for k,v in fund_in.items()])
	
def strToFund(str_in):
	"""Returns an Investment object from its symbol, str_in."""
	if str_in in market['symbols'].keys():
		return market['symbols'][str_in]
	return str_in
	
def notFund(fund, words):
	"""Returns a message if fund is not an existing Investment object."""
	if fund not in market['funds']:
		return "You tried to %s a nonexistent fund." % (words)
	
def putDate():
	"""Returns the current date as a string."""
	return str(datetime.today())[0:10]
	
def putTime():
	"""Returns the current time as a string."""
	return str(datetime.now().time())[0:8]
	
def timeStamp():
	"""Returns the current date and time as a string."""
	return 'At ' + putDate() + ', on ' + putTime() + ', '
	
def printMarket():
	"""Prints all existing Investment symbols and their price."""
	for fund in market['funds']: print fund.symbol, ': ', fund.price
	
class Portfolio(object):
	"""A Portfolio object has the following attributes:
	Portfolio.balance: The portfolio's cash stored as a floating point number. 
	Portfolio.stocks: A dictionary of every Stock.symbol and shares owned.
	Portfolio.mutualFunds: A similar dictionary for every MutualFund.symbol.
	Portfolio.auditLog: A timestamped list, in order, of every time the 
		Portfolio's balance or shares of an Investment have changed."""
	def __init__(self):
		self.balance = 0.0
		self.stocks = {}
		self.mutualFunds = {}
		self.auditLog = [] 
		portfolios.append(self)
		
	def __str__(self):
		return ("\nYour portfolio contains:\n\tCash: $%.2f\n\tStocks: " 
		% (self.balance) + unDict(self.stocks) + "\n\tMutual Funds: " 
		+ unDict(self.mutualFunds) + "\n")

	def __repr__(self):
		return self.__str__()
		
	def cashOp(self, cash, sign, words):
		"""Changes a Portfolio balance and appends the auditLog"""
		self.balance += cash * sign
		self.auditLog.append(timeStamp() + "%.2f was %s your cash balance." 
		% (cash, words))
		return self.auditLog[-1]
	
	def addCash(self, cash):
		"""Increases a Portfolio balance and appends the auditLog"""
		return self.cashOp(float(cash), 1, 'added to')
		
	def withdrawCash(self, cash):
		"""Decreases a Portfolio balance and appends the auditLog, but will
		not permit an overdraw"""
		if cash > self.balance:
			self.auditLog.append(timeStamp() + "an overdraw was attempted.")
			return self.auditLog[-1]
		return self.cashOp(float(cash), -1, 'withdrawn from')
		
	def buy(self, shares, fund, fundList):
		"""If fund is an Investment object or an Investment.symbol,
		decreases the Portfolio.balance by the Investment.price * shares and
		increases the number of shares of the Investment in the Portfolio"""
		fund = strToFund(fund)
		notFund(fund, 'buy')
		if shares * fund.price > self.balance: 
			return self.withdrawCash(shares * fund.price)
		fundList[fund.symbol] += shares
		self.withdrawCash(shares * fund.price)
		self.auditLog.append(timeStamp() 
		+ "you bought %s shares of %s." % (str(shares), fund.symbol))
		return self.auditLog[-1]
		
	def buyStock(self, shares, fund):
		"""Calls Portfolio.buy for a Stock object or Stock.symbol"""
		return self.buy(int(shares), fund, self.stocks)
		
	def buyMutualFund(self, shares, fund):
		"""Calls Portfolio.buy for a MutualFund object or MutualFund.symbol"""
		return self.buy(float(shares), fund, self.mutualFunds)
	
	def sell(self, fund, shares, fundList, sellPrice):
		"""If fund is an Investment object or an Investment.symbol,
		increases the Portfolio.balance by sellPrice * shares and
		decreases the number of shares of the Investment in the Portfolio, but
		does not allow more shares to be sold than are in the Portfolio"""
		fund = strToFund(fund)
		notFund(fund, 'sell')
		if fundList[fund.symbol] < shares:
			return "You tried to sell shares you do not own."
		fundList[fund.symbol] -= shares
		self.addCash(shares * sellPrice)
		self.auditLog.append(timeStamp() + "you sold %s shares of %s." % 
		(str(shares),fund.symbol))
		return self.auditLog[-1]
		
	def sellStock(self, fund, shares):
		"""Calls Portfolio.sell for a Stock object or Stock.symbol"""
		return self.sell(fund, shares, self.stocks, (shares * uniform(0.5 * 
		strToFund(fund).price, 1.5 * strToFund(fund).price)))
		
	def sellMutualFund(self, fund, shares):
		"""Calls Portfolio.sell for a MutualFund or MutualFund.symbol"""
		return self.sell(fund, shares, self.mutualFunds, uniform(0.9, 1.2))
		
	def history(self):
		"""Prints the auditLog"""
		print "\nAudit log history:\n\t" + "\n\t".join(self.auditLog) + "\n"
		
class Investment(object):
	"""All object of class Investment and subclasses Stock and MutualFund have
	the following attributes:
	Investment.price: The price to buy one share of the Investment
	Investment.symbol: A string traders can use to refer to the Investment
	Initializing an instance of an Investment or one of its subclasses adds
	the Investment to the market"""
	def __init__(self, price, symbol, fundkey):
		self.price = price
		self.symbol = str(symbol)
		market[fundkey] = self
		market['symbols'][self.symbol] = self
		market['funds'][self] = fundkey
		
	def __str__(self, words):
		return (self.symbol + ' is a %s you can buy at ' % (words) 
		+ str(self.price) + ' per share.')
		
	def __repr__(self):
		return self.__str__()
	
class Stock(Investment):
	"""Initializing an instance of a Stock, in addition to the actions taken
	by calling Investment.__init__, adds 0 shares of the Stock to every
	Portfolio object's Portfolio.stocks"""
	def __init__(self, price, symbol):
		Investment.__init__(self, price, symbol, 'stocks')
		for p in portfolios: p.stocks[symbol] = 0
		
	def __str__(self):
		return Investment.__str__(self, 'stock')
		
	def __repr__(self):
		return self.__str__()
		
class MutualFund(Investment):
	"""Initializing an instance of a MutualFund, in addition to the actions 
	taken by calling Investment.__init__, adds 0.0 shares of the MutualFund
	to every Portfolio object's Portfolio.mutualFunds"""
	def __init__(self, symbol):
		Investment.__init__(self, 1, symbol, 'mutualFunds')
		for p in portfolios: p.mutualFunds[symbol] = 0.0
		
	def __str__(self):
		return Investment.__str__(self, 'mutual fund')
		
	def __repr__(self):
		return self.__str__()