# page 242
def fix_unicode(text):
	return text.replace(u"\u2019","'")

from bs4 import BeautifulSoup
import requests
import re
from collections import defaultdict
import random

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

# We now have all periods and words in the essay ordered into a list

# We call a "bigram" an ordered pair of successive words

# The bigram model: Given some starting word, we look at all the
# words that follow it in the source documents. We randomly choose
# one of these to be the next word, and we repeat the process until
# we get to a period, which signifies the end of the sentence. To get
# a starting word, we randomly pick a word that follows a period.

# Recall that zip stops when any of its inputs is done, so that
# zip(document, document[1:]) gives us precisely the pairs of
# consecutive elements of document as a list

bigrams = zip(document, document[1:])
transitions = defaultdict(list)
for prev, current in bigrams:
	transitions[prev].append(current)

# Now <transitions> is a list whose elements have the form
# (word, list of successors of that word)

def generate_using_bigrams():
	current = "."
	result = []
	while True:
		next_word_candidates = transitions[current]	# bigrams (current, _)
		current = random.choice(next_word_candidates)
		result.append(current)
		if current == ".": return " ".join(result)

# Now we repeat the process with trigrams
trigrams = zip(document, document[1:], document[2:])
trigram_transitions = defaultdict(list)
starts = []

# Generate list of sentence starter words and list of transitions
for prev, current, next in trigrams:
	if prev == ".":
		starts.append(current)
	trigram_transitions[(prev,current)].append(next)

def generate_using_trigrams():
	current = random.choice(starts)	# choose a random starting word
	prev = "."
	result = [current]
	while True:
		next_word_candidates = trigram_transitions[(prev,current)]
		next_word = random.choice(next_word_candidates)

		prev, current = current, next_word
		result.append(current)

		if current == ".":
			return " ".join(result)
print(generate_using_trigrams())