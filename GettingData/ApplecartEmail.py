from bs4 import BeautifulSoup
import requests
url = "http://applecart.co/"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
print(soup)