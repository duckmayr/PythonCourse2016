import re

#re.findall and re.split

file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()





mytext=''.join(text)

re.split(r'\d',mytext)
re.split(r'\d\.',mytext)

re.findall(r'[a-z]',mytext)
re.findall(r'[a-z]+',mytext)
re.findall(r'[A-Z]',mytext)
re.findall(r'[A-Z]+',mytext)
re.findall(r'[A-Z]+.',mytext)
re.findall(r'\d',mytext)
re.findall(r'\d+',mytext)
re.findall(r'\d+.',mytext)
re.findall(r'\d+.*',mytext)
re.findall(r'\d+.*\w',mytext)
re.findall(r'\d\w',mytext)
re.findall(r'(\d+\S*)',mytext)




# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

#re.compile

pattern = re.compile(r'[a-z]+') #Create a regex object

pattern.split(mytext)
pattern.findall(mytext)

#re.MULTILINE

mytext='bin\nban\ncan'

pattern = re.compile(r'^b\w*')
pattern.findall(mytext)

pattern = re.compile(r'^b\w*',re.MULTILINE)
pattern.findall(mytext)

re.findall(r'^b\w*',mytext,re.MULTILINE)

#re.match and re.search

mytext = 'a1b2c3D'

re.match(r'\d',mytext) #matches the pattern at the beginning of the string
re.search(r'\d',mytext) #looks for the pattern anywhere in the string

#math and search

pattern = re.compile(r'\d')

pattern.match(mytext) #similar to above
pattern.match(mytext,1) #matches the pattern in the position 1

pattern.search(mytext) #similar to above
pattern.search(mytext, 1) #looks for the pattern in the position 1

pattern = re.compile('r[A-Z]')
pattern.search(mytext,1,6) #looks for the pattern between positions 1 and 5

#create groups

mytext = '12 twelve'

pattern = re.compile(r'(\d*)\s(\w*)')
mysearch=pattern.search(mytext)
mysearch.groups() #list of all groups
mysearch.group(0) #the complete match
mysearch.group(1) #the first group
mysearch.group(2) #the second group

pattern = re.compile(r'(?P<number>\d*)\s(?P<name>\w*)')
mysearch=pattern.search(mytext)
mysearch.groups()
mysearch.groupdict()

mytext = '12 24'
pattern = re.compile(r'(\d*)')
pattern.search(mytext).groups()
pattern.search(mytext).group(0)
pattern.search(mytext).group(1)


mytext = '12 24'
pattern = re.compile(r'(\d*)\s(\d*)')
pattern.search(mytext).groups()
pattern.search(mytext).group(0)
pattern.search(mytext).group(1)
pattern.search(mytext).group(2)

