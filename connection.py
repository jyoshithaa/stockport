# Import necessary libraries
import tweepy
from textblob import TextBlob

# Set up Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the stock you want to analyze
stock_symbol = 'AAPL'

# Define a function for sentiment analysis
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Real-time sentiment analysis
def real_time_sentiment_analysis(stock_symbol):
    tweets = api.search(q=stock_symbol, count=100)

    positive_count = 0
    neutral_count = 0
    negative_count = 0

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet.text)
        if sentiment == 'Positive':
            positive_count += 1
        elif sentiment == 'Neutral':
            neutral_count += 1
        elif sentiment == 'Negative':
            negative_count += 1

    total_tweets = len(tweets)

    print(f"Stock Symbol: {stock_symbol}")
    print(f"Total Tweets Analyzed: {total_tweets}")
    print(f"Positive Sentiment: {positive_count / total_tweets * 100}%")
    print(f"Neutral Sentiment: {neutral_count / total_tweets * 100}%")
    print(f"Negative Sentiment: {negative_count / total_tweets * 100}%")

if _name_ == "__main__":
    real_time_sentiment_analysis(stock_symbol)