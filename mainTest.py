from sentiment_analysis_spanish import sentiment_analysis

print('making class')
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print('printing model')
print(sentiment.sentiment("me gusta la tombola es genial"))

