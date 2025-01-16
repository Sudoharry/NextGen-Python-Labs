from textblob import TextBlob
import nltk

with open('myfile.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)


## This is esentially how you can analyze articles from the web 