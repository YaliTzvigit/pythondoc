
# Recup avec autre methode >

from bs4 import BeautifulSoup

import requests

# url :

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

# Affichez les données > 

print(soup)

table = soup.find_all('table') [1] # Les 1er elements du 'table'

print(table)

soup.find_all('th')
