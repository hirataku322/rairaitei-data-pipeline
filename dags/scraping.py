import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://www.rairaitei.co.jp/store/list.php")
soup = BeautifulSoup(page.content, "html.parser")
stores = soup.find_all("div", class_="store_list_box")

names, addresses, prefectures, zip_codes = [], [], [], []
for store in stores:
    name = store.h4.text

    address = store.find("li", class_="store_add").text.replace('住所', '')

    prefecture_element = re.match('東京都|北海道|(?:京都|大阪)府|.{2,3}県' , address)
    prefecture = prefecture_element.group() if prefecture_element else None

    zip_code_element = requests.get(f'https://api.excelapi.org/post/zipcode?address={address}')
    zip_code = zip_code_element.text if zip_code_element else None

    names.append(name)
    addresses.append(address)
    prefectures.append(prefecture)
    zip_codes.append(zip_code)

df = pd.DataFrame({'name': names, 'address': addresses, 'prefectures': prefectures, 'zip_code': zip_codes})
df.to_csv('rairaitei.csv', index=False, encoding='utf-8')
