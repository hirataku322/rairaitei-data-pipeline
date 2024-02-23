import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.rairaitei.co.jp/store/list.php")
soup = BeautifulSoup(page.content, "html.parser")
stores = soup.find_all("div", class_="store_list_box")

names = []
addresses = []
for store in stores:
    names.append(store.h4.text)
    addresses.append(store.find_all("li", class_="store_add")[0].text)

print(names)
