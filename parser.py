
from bs4 import BeautifulSoup 
import requests

response = requests.get("https://pythonhelp.ru/python/kak-napisat-parser-na-python/")
html = response.text
soup = BeautifulSoup(html, "html.parser")

elements = soup.find_all("HTML-код")

for element in elements:
    content = element.text
    print(content)