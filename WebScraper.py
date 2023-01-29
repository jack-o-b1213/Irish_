from bs4 import BeautifulSoup
import requests
import json


def generateJson():
    page = 0
    housingArr = []
    while page < 15500:
        print(page)
        url = f'https://www.daft.ie/property-for-sale/ireland?pageSize=0&from={page}'
        response = requests.get(url, timeout=20)
        content = BeautifulSoup(response.content, "html.parser")

        ads = content.findAll('li', attrs={"class": "SearchPage__Result-gg133s-2 itNYNv"})

        for ad in ads:
            house = {
                "price": ad.find('div', attrs={"data-testid": "price"}).text,
                "address": ad.find('p', attrs={"data-testid": "address"}).text
            }
            housingArr.append(house)

        page += 20

    with open('data/housingPrices.json', 'w') as outfile:
        json.dump(housingArr, outfile)
