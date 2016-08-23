import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "
# TODO: print lines that contain a word of any length starting with s and ending with e

keyword = re.compile(r'the ')
for line in text:
	if not keyword.search(line):
		print line
keyword = re.compile(r'\ss[a-zA-Z]*e\s')
for line in text:
	if keyword.search(line):
		print line
  
# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY
pieces = re.compile(r'\.').split(date)
print 'Month: %s\nDay: %s\nYear: %s' %(pieces[0], pieces[1], pieces[2])

# TODO: Write a regular expression that finds html tags in example.html and print them.
# find all hrefs within links
file = open("C:/Users/owner/Documents/GitHub/MyPython/PythonCourse2016/Day4/Docket05-1.html", "r")
text = file.readlines()
file.close()
pattern = re.compile(r'<a.*>')
aTags = []
for line in text:
	if len(pattern.findall(line)) > 0: aTags.append(pattern.findall(line))
newPattern = re.compile(r'href="[^>]*"')
for item in aTags:
	for tag in item:
		newPattern.findall(tag)

# TODO: Scrape a website and search for some things...

## This is adapting some things from my HW2 to look at district court cases. It still needs some work. ##
from bs4 import *
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
	
def getSurrounding(pattern, opinion, cite, surrounding, case):
	"""This gets the opinion text surrounding a citation."""
	pieces = [x for x in re.split(pattern, opinion) if x not in cite]
	for i in range(len(pieces)):
		if len(pieces) - i > 1:
			surrounding[case].append(pieces[i][-100:] + cite[i] + pieces[i+1][:100])
	
home_address = 'http://law.justia.com'
web_address = home_address + '/cases/federal/district-courts/'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read(), 'html.parser')
heading = soup.find_all('h4', text = 'Browse Opinions From the U.S. Federal District Courts')[0]
for sibling in heading.next_siblings:
	if hasattr(sibling, 'children'):
		for child in sibling.children:
			if hasattr(child, 'find_all'):
				links = child.find_all('a')
linkURLs = dict()
for i in range(len(links)):
	linkURLs[int(enc(links[i].get_text()))] = home_address + enc(links[i].get('href'))
tmp_page = urllib2.urlopen(linkURLs[2000])
tmp_soup = BeautifulSoup(tmp_page.read())
heading = tmp_soup.find_all('h4', text = 'Opinions From the U.S. Federal District Courts')[0]
for sibling in heading.next_siblings:
	if hasattr(sibling, 'children'):
		for child in sibling.children:
			if hasattr(child, 'find_all'):
				links = child.find_all('a')
stateURLs = dict()
for i in range(len(links)):
	stateURLs[enc(links[i].get_text())] = home_address + enc(links[i].get('href'))
reporters = ['U\.\sS\.', 'U\.S\.', 'S\.\sCt\.', 'L\.\sEd\.', 'L\.\sEd\.\s2d', 'Dallas', 'Cranch', 'Wheat\.', 'How\.', 'Black', 'Wall\.']
tmp_page = urllib2.urlopen(stateURLs['Missouri'])
tmp_soup = BeautifulSoup(tmp_page.read())
districtURLs = dict()
for item in tmp_soup.find_all(class_='indented'):
	links = item.find_all('a')
for i in range(len(links)):
	districtURLs[enc(links[i].get_text())] = home_address + enc(links[i].get('href'))
tmp_page = urllib2.urlopen(districtURLs['U.S. District Court for the Eastern District of Missouri'])
tmp_soup = BeautifulSoup(tmp_page.read())
results = tmp_soup.find_all(class_ = 'has-padding-content-block-30 -zb')
cites = surrounding = cases = {}
for i in results:
	cases[enc(i.a.text)] = home_address + enc(i.a.get('href'))
for case in cases.keys():
	if len(cases[case]) > 0:
		tmp_page = urllib2.urlopen(cases[case])
		tmp_soup = BeautifulSoup(tmp_page.read(), 'html.parser')
		opinion = enc(tmp_soup.find_all('div', id = 'opinion')[0].text)
		cites[case] = []
		surrounding[case] = []
		for i in range(len(reporters)):
			pattern = re.compile(r'([0-9]*[\s]%s[ ][0-9_]*)'%(reporters[i]))
			cite = pattern.findall(opinion)
			if i == 0: cites[case] = cite
			else: 
				if len(pattern.findall(opinion)) > 0: cites[case].extend(cite)
			getSurrounding(pattern, opinion, cite, surrounding, case)
		with open('lab8_duckmayr.csv', 'ab') as f:
			my_writer = csv.DictWriter(f, fieldnames=("casename", "cited_case_citation", "surrounding_text"))
			my_writer.writeheader()
			for case in cites.keys():
				try:
					for i in range(len(cites[case])):
						my_writer.writerow({"casename":case, "cited_case_citation":cites[case][i], "surrounding_text":surrounding[case][i]})
				except: pass
