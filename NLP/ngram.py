from bs4 import BeautifulSoup
import requests

def fix_unicode(text):
	return text.replace(u"\u2019","'")

url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

content = soup.find("div", "entry-content")
regex = r"[\w']+|[\.]"

for paragraph in content("p"):
	words = re.findall(regex, fix_unicode(paragraph.text))
	document.extend(words)