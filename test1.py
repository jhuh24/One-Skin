from bs4 import BeautifulSoup
from selenium import webdriver

# from selenium.webdriver.chrome.service import Service
# ser = Service(r'c:\path\to\windows\webdriver\executable.exe')
# op = webdriver.ChromeOptions()
# s = webdriver.Chrome(service=ser, options=op)

import pandas as pd

driver = webdriver.Chrome(executable_path='c:\path\to\windows\webdriver\executable.exe')

driver.get('https://doctor.webmd.com/providers/specialty/dermatology/california/san-diego')

# 'https://doctor.webmd.com/providers/specialty/dermatology/california/berkeley'

results = []
other_results = []
rating = []
city = []
Zip = []

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for element in soup.findAll(attrs={'class': 'prov-name-wrap'}):
    name = element.find('a')
    results.append(name.text)

for element2 in soup.findAll(attrs={'class': 'prov-addr-dist'}):
    name2 = element2.find('span')
    other_results.append(name2.text)

for element3 in soup.findAll(attrs={'class': 'prov-ratings-wrap'}):
    name3 = element3.find('div', {'role': 'slider'})
    name4 = name3.attrs['aria-valuenow']
    # print(name4)
    # print(len(rating))
    rating.append(name4)


for loc in other_results:
    x = loc.split(",")

    if len(x) > 2:
        city.append(x[1])
        y = x[2]
        z = y.split()
        Zip.append(z[1])
    else:
        city.append(x[0])
        y = x[1]
        z = y.split()
        Zip.append(z[1])

    # print(z)

df = pd.DataFrame({'Name': results, 'Location': other_results, 'City': city, 'Zip Code': Zip, 'Rating': rating})
df.to_excel('Dermatologists_San_Diego.xlsx', index=False)

# for ele in results:
#     print(ele)

# for e in other_results:
#     print(e)

