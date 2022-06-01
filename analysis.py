from requests_html import HTMLSession
from textblob import TextBlob
import pandas as pd

s = HTMLSession()

data = []
u = open('urls.txt', 'r')
urls = u.readlines()
for url in urls:
	r = s.get(url.strip())
	content = r.html.find('div.td-post-content', first=True).text
	sen = TextBlob(content)
	pol = sen.sentiment.polarity
	if pol < 0:
		sent = 'Negative'
	elif pol==0:
		sent = 'Neutral'
	else:
		sent = 'Positve'

	sub = sen.sentiment.subjectivity
	data.append([url.strip(), content, pol, sub, sent])

df = pd.DataFrame(data, columns=['Url', 'Text', 'Polarity', 'Subjectivity', 'Sentiment'])
df.to_csv('Sentiment analysis dataset.csv', index=False)