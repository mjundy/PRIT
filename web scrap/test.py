from urllib.request import urlopen
from bs4 import BeautifulSoup
wiki_link = "http://10.35.1.88"
html = urlopen(wiki_link).read()
soup = BeautifulSoup(html, 'html.parser')
categories_table = soup.find("span", {"id": "temperature"})
for each in categories_table.findAll("p"):
    print(each.text)