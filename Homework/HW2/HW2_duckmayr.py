"""I intend this to be a very small start to an ambitious project I intend to continue working on for some time. 
Courts often cite prior court opinions from themselves or other courts. 
When judicial scholars study this behavior, they often rely on LexisNexis' Shepard's service, which collects citation information. 
However, it was made with lawyers' needs in mind, not political scientists. It has things we don't need and doesn't have things we want.
For example, say that case X has cited case Y. 
Shepard's will document every page of case X with a reference to case Y, but not the number of times case Y was cited on that page. 
Using Shepard's data, case X citing case Y 5 times on one page would be observationally equivalent to case X citing case Y 2 times.

Ultimately, I will have a function that will create a csv with one row for every instance one case cites another case.
The function will ask the user the range of years and courts for which (s)he wants information and write a csv.
For this homework assignment, it will only scrape Supreme Court opinions. 
Also, it does not work on sufficiently old Court opinions yet (it does work for at least the last twenty years though)
I have some code commented out for that reason, and a note about why it's commented out.
At the end, I have commented out code that I ran to create the csv 'HW2_duckmayr.csv', which is a test run of the function for the years 2000-2005."""

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import csv
import unicodedata

def enc(uIn):
	"""Given unicode input (uIn), this function normalizes it and encodes it (i.e. returns a normalized, encoded string)"""
	return unicodedata.normalize('NFKD', uIn).encode('utf-8')

def splitReg(start, end, uIn):
	"""This function cleans up the dates and docket numbers."""
	return enc(re.compile(r'%s([^)]*)%s'%(start, end)).findall(uIn)[0]).strip()
	
def docketOrUS(uIn):
	"""This function determines whether U.S. reports publication information is available for the citing case, or just the docket number."""
	if len(re.compile(r'%s([^)]*)%s'%('n:', '\nC')).findall(uIn)) > 0: return 'US'
	return 'Docket'
	
def getSurrounding(pattern, opinion, cite, surrounding, case):
	"""This gets the opinion text surrounding a citation."""
	pieces = [x for x in re.split(pattern, opinion) if x not in cite]
	for i in range(len(pieces)):
		if len(pieces) - i > 1:
			surrounding[case].append(pieces[i][-100:] + cite[i] + pieces[i+1][:100])
	
def getCites(fileName):
	"""Asks the user for the years and courts for which (s)he wants citation data and writes the data to fileName."""
	years = input("What years do you want citation data for? Provide the first year and the last year as a list: ") 
	if type(years) == int: years = [years] #In case they only want one year and don't put it in a list
	# The lines below are commented out because I only have the code written for the Supreme Court so far
	## courts = input("What courts do you want citation data for? Available options are 'supreme court', 'appellate courts', 'district courts', and 'state courts'. Provide them as a list: ")
	## if type(courts) == str: courts = [courts] # In case they only want data for one type of court and don't put it in a list
	courts = ['supreme court'] # Since I'm not giving the user options yet, I'm temporarily setting this as the only option I've set it up for
	if len(years) < 2: years = [years[0], years[0]] # In case they only want one year and only gave one year
	for year in range(years[0], years[1]+1):
		reporters = ['U\.\sS\.', 'U\.S\.', 'S\.\sCt\.', 'L\.\sEd\.', 'L\.\sEd\.\s2d', 'Dallas', 'Cranch', 'Wheat\.', 'How\.', 'Black', 'Wall\.']
		for court in courts:
			cases = {}
			dates = {}
			citation = {}
			docket = {}
			pcCases = []
			otherCases = {}
			if court == 'supreme court':
				home_address = 'https://supreme.justia.com'
				web_address = home_address + '/cases/federal/us/year/' + str(year) + '.html'
				web_page = urllib2.urlopen(web_address)
				soup = BeautifulSoup(web_page.read(), 'html.parser')
				results = soup.find_all(class_ = 'has-padding-content-block-30 -zb search-result')
				for i in results:
					cases[enc(i.a.text)] = home_address + enc(i.a.get('href'))
					docket[enc(i.a.text)] = docketOrUS(i.text)
					if docketOrUS(i.text) == 'Docket': citation[enc(i.a.text)] = 'Docket No. ' + splitReg('r:', '\nC', i.text)
					else: citation[enc(i.a.text)] = splitReg('n:', '\nC', i.text)
					dates[enc(i.a.text)] = splitReg('e:', '\n\n\n\t\t\t\t\t\th', i.text)
				cites = {}
				surrounding = {}
				for case in cases.keys():
					if docket[case] == 'US':
						try: tmp_page = urllib2.urlopen(cases[case] + 'case.html')
						except: 
							try: tmp_page = urllib2.urlopen(cases[case] + 'opinion.html')
							except: tmp_page = urllib2.urlopen(cases[case])
					if docket[case] == 'Docket':
						tmp_page = urllib2.urlopen(cases[case])
						tmp_soup = BeautifulSoup(tmp_page.read())
						nav = tmp_soup.find_all('nav', class_ = 'breadcrumbs font-helvetica small-font')[0].text
						if 'Per Curiam' in nav: pcCases.append(case)
						lis = tmp_soup.find_all('li')
						for li in lis:
							if 'Opinion' in li.text: otherCases[case] = enc(li.a.get('href'))
						if case in pcCases: tmp_page = urllib2.urlopen(cases[case])
						if case in otherCases: tmp_page = urllib2.urlopen(cases[case] + otherCases[case])
					tmp_soup = BeautifulSoup(tmp_page.read(), 'html.parser')
					try: opinion = enc(tmp_soup.find_all('div', id = 'opinion')[0].text)
					except: 
						print 'Could not scrape %s.' %(case)
						continue
					cites[case] = []
					surrounding[case] = []
					for i in range(len(reporters)):
						pattern = re.compile(r'([0-9]*[\s]%s[ ][0-9_]*)'%(reporters[i]))
						cite = pattern.findall(opinion)
						if i == 0: cites[case] = cite
						else: 
							if len(pattern.findall(opinion)) > 0: cites[case].extend(cite)
						getSurrounding(pattern, opinion, cite, surrounding, case)
				with open(fileName, 'ab') as f:
					my_writer = csv.DictWriter(f, fieldnames=("court", "citing_case_year", "casename", "citing_usid", "cited_case_citation", "surrounding_text"))
					my_writer.writeheader()
					for case in cites.keys():
						try:
							for i in range(len(cites[case])):
								my_writer.writerow({"court":court, "citing_case_year":year, "casename":case, "citing_usid":citation[case], "cited_case_citation":cites[case][i], "surrounding_text":surrounding[case][i]})
						except: pass
#
getCites('HW2_duckmayr.csv')
## then, when I ran it, it prompted me for the years I wanted to get data for; I entered [2000,2005] to get the csv