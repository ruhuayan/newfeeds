from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
'''
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
''''

class Sentiment:
  	def __init__(self, instances=100):
		self._instance = instances
    	pass
	'''
	def _getAdjective(text):	
		pass
	'''
	
	def analysis(content):
		sentents = sent_tokenize(content)
		sid = SentimentIntensityAnalyzer()
		for sentence in sentences:
			print(sentence)
			ss = sid.polarity_scores(sentence)
			for k in sorted(ss):
			print('{0}: {1}, '.format(k, ss[k]))
			print()
		