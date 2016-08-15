#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page

## The following works, but isn't in functions: ##

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import csv

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
headings = soup.find_all('h3')
with open('lab4_duckmayr.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("name", "specialization", "title", "email", "website"))
	my_writer.writeheader()
	for i in range(len(headings)):
		for j in headings[i].next_siblings:
			if j.name == 'h3': break
			if j.name == 'div': 
				name = str(j.a.text)
				specialization = headings[i].text.encode('utf-8')
				title = str(j.text).split('\n')[-1].strip()
				tmp_page = str(web_address)[:25]+ j.a.get('href').encode('utf-8')
				tmp_page = urllib2.urlopen(str(tmp_page))
				tmp_soup = BeautifulSoup(tmp_page.read())
				tmp_labels = tmp_soup.find_all(class_='field-label')
				for k in range(len(tmp_labels)):
					textContent = tmp_labels[k].text.encode('utf-8')
					if 'E-mail' in textContent:
						email = tmp_labels[k].next_sibling.text.encode('utf-8')
					if 'Website' not in textContent:
						website = 'NA'
					else:
						website = tmp_labels[k].next_sibling.a.get('href').encode('utf-8')
				my_writer.writerow({"name":name, "specialization":specialization,"title":title,"email":email,"website":website})
