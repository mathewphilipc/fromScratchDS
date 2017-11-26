from bs4 import BeautifulSoup
import requests
url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
#print(url)
print(soup)
# A good first step is to find all of the td thumbtext tag elements
tds = soup('td', 'thumbtext')
print len(tds)