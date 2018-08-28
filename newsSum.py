import urllib2
from bs4 import BeautifulSoup
from summarize import FrequencySummarizer
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_only_text(url):
 	page = urllib2.urlopen(url).read().decode('utf8')
 	soup = BeautifulSoup(page)
 	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 	return soup.title.text, text

def analysis(analyzer, content):
	sentences = sent_tokenize(content)
	for sentence in sentences:
		print(sentence)
		ss = analyzer.polarity_scores(sentence)
		for k in sorted(ss):
			print('{0}: {1}, '.format(k, ss[k]))
		print()
		
feed_xml = urllib2.urlopen('http://rss.cnn.com/rss/cnn_world.rss').read()
#feed_xml = urllib2.urlopen('http://rss.radio-canada.ca/fils/nouvelles/international.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'), "lxml")
to_summarize = map(lambda p: p.text, feed.find_all('guid'))

#print to_summarize

fs = FrequencySummarizer()
analyzer = SentimentIntensityAnalyzer()

for article_url in to_summarize[:5]:
  	title, text = get_only_text(article_url)
  	print '----------------------------------'
  	print title
  	for s in fs.summarize(text, 2):
   		print '*',s
		print '********************************'
		analysis(analyzer, s)
		
