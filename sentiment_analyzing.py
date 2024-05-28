import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
sia=SentimentIntensityAnalyzer()
data=['i am feeling good','having some problems lately','haha life is just...','making some progress']
for d in data:
     ss=sia.polarity_scores(d)
     print(d)
     for k in ss:
          print(k,ss[k])
