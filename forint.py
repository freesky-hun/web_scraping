import requests
from bs4 import BeautifulSoup

url = "https://www.wisselkoers.nl/hongaarse_forint"

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        euro_unit = soup.find("span", class_="euro-unit")
        if euro_unit:
            exchange_rate = euro_unit.get_text()
            print(exchange_rate)
        else:
            print("Exchange rate not found on the page.")
    else:
        print("Failed to retrieve the webpage.")
except Exception as e:
    print("An error occurred:", str(e))
