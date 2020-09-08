import requests
from bs4 import BeautifulSoup
# "http://www.pyclass.com/example.html", 
# headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) 
# Gecko/20100101 Firefox/61.0'}
req = requests.get('http://www.pyclass.com/example.html',headers=\
    {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0)Gecko/20100101 Firefox/61.0'})
cont = req.content
# print(cont)

soup = BeautifulSoup(cont, "html.parser")
# print(soup.prettify())

divs = soup.find("div")
cities = soup.find("div",{"class":"cities"})
all_cities = soup.find_all("div",{"class":"cities"})
first_city = soup.find_all("div",{"class":"cities"})[0]
# print(divs)
# print("---------------------")
# print(cities)
# print("---------------------")
# print(all_cities)
# print("---------------------")
# print(first_city)
print(all_cities[0].find_all("h2"))
print(all_cities[0].find_all("h2")[0].text)