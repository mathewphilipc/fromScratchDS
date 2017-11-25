from bs4 import BeautifulSoup
import requests
url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')