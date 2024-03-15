from bs4 import BeautifulSoup
import pandas as pd
import requests as req

url = "https://www.worldometers.info/world-population/population-by-country"

resp = req.get(url)

soup = BeautifulSoup(resp.text, "lxml")

rows = soup.find('table', {'id': 'example2'}).find('tbody').find_all('tr')

countries_list = []

for row in rows:
    details = {}

    details['Name'] = row.find_all('td')[1].text
    details['Population'] = row.find_all('td')[2].text.replace(",","")
    details['Area'] = row.find_all('td')[6].text.replace(",","")
    details['Migrants'] = row.find_all('td')[7].text.replace(",","").replace("-","")
    details['Median Age'] = row.find_all('td')[9].text
    details['Urban Population(%)'] = row.find_all('td')[10].text.replace("%","").replace(" ","")
    details['World Share(%)'] = row.find_all('td')[11].text.replace("%","").replace(" ","")

    countries_list.append(details)

df = pd.DataFrame(countries_list)
df.to_csv('countries_data.csv', index=False)

print("Data Scraped🎉🎉")
