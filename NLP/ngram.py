# page 242
def fix_unicode(text):
	return text.replace(u"\u2019","'")

from bs4 import BeautifulSoup
import requests
import re

url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html = requests.get(url).text

# To get data out of HTML, we will use the BeautifulSoup library,
# which builds a tree out of the various elements on a web page and
# provides a simple interface for accessing them.

soup = BeautifulSoup(html, 'html5lib')

# Book says to use:
# content = soup.find("div", "entry-content")
# But web page seems to have changed since this printing. This works:

content = soup.find('div', {'class' : 'article-body'})

# This returns the first page element of type div with such that
# class = 'article-body'



# Once we get the text of the web page, we'll want to split it into a
# sequence of words and periods (so that we can tell where the
# sentences end). We can do this using re.findall()


regex = r"[\w']+|[\.]"

document = []

for paragraph in content("p"):
	words = re.findall(regex, fix_unicode(paragraph.text))
	document.extend(words)


print(document)