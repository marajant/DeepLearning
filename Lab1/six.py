from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

r = requests.get("http://" +url)

data = r.text
lst = []
soup = BeautifulSoup(data)
all_tables=soup.find_all('table')
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    links = row.findAll('a')
    lst.append(cells)
fo = str(lst)
a = open('states.txt', 'w')
a.write(fo)
a.close()

