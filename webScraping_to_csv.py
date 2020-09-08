import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get('http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/',\
    headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0)\
        Gecko/20100101 Firefox/61.0'})
content = req.content
# print(cont)

sou = BeautifulSoup(content,"html.parser")
# print(sou)
# print(sou.prettify())

pages = sou.find_all("a",{"class":"Page"})
page_count = int(pages[-1].text)
# print(pages[-1].text)
# print(len(pages))

details = []
idx = 1
base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,page_count*10,10):
    reqs = requests.get(base_url+str(page)+".html",headers={'User-agent': \
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0)Gecko/20100101 \
                Firefox/61.0'})
    cont = reqs.content
    soup = BeautifulSoup(cont, "html.parser")
    all_props = soup.find_all("div",{"class":"propertyRow"})
    for props in all_props:
        temp = {}
        # print(f'Property {idx}')
        temp['Address'] = props.find_all("span",{"class":"propAddressCollapse"})\
                            [0].text
        try:
            temp['Locality'] = props.find_all("span",{"class":"propAddressCollapse"})\
                            [1].text
        except:
            temp['Locality'] = "N/A"
        temp['Price']= props.find("h4",{"class":"propPrice"}).text.replace\
                        ("\n","").strip()
        try:
            temp['Beds'] = props.find("span",{"class":"infoBed"}).\
                find("b").text
        except:
            temp['Beds'] = "N/A"
        try:
            temp['Area'] = props.find("span",{"class":"infoSqFt"}).\
                find("b").text
        except:
            temp['Beds'] = "N/A"
        try:
            temp['Full Baths'] = props.find("span",{"class":"infoValueFullBath"}).\
                find("b").text
        except:
            temp['Beds'] = "N/A"
        try:
            temp['Half Baths'] = props.find("span",{"class":"infoValueHalfBath"}).\
                find("b").text
        except:
            temp['Beds'] = "N/A"
        col_grp = props.find_all("div",{"class":"columnGroup"})
        # print(col_grp)
        for col in col_grp:
            # print(col)
            grp = col.find("span", {"class": "featureGroup"})
            if grp:
                if "Lot Size" in grp.text:
                    size = col.find("span", {"class": "featureName"}) 
                    temp['Lot Size'] = size.text
        # print(f'Property {idx} End')
        details.append(temp)
# print(details)

#coneverting the details list into a dataframe.
df = pd.DataFrame(details)
# print(df.head())
df.to_csv('F:\Python_Applications_Udemy\Web Scraping\properties.csv')
# print("Done")




