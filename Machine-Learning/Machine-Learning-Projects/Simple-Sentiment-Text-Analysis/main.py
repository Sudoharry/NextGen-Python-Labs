from textblob import TextBlob
from newspaper import Article
import nltk

url = 'https://patch.com/new-jersey/jersey-city/murder-charge-man-connection-fatal-hudson-county-shooting'
article = Article(url)

nltk.download('punkt_tab')

article.download()
article.parse()
article.nlp()

text = article.summary  ## Get the article's text or summary
print(text)


blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)

## This is esentially how you can analyze articles from the web 