import tweepy

#go to tweepy docs and 'clics get started', copy the EX

auth = tweepy.OAuth1UserHandler('kApuYwQaXGCRuZNoVi66pVmfN','xihxbofSRLDshyEKJhXQX0rDodd094825NpiV7KQquOibkaGlV','1694296214097842177-fEZFpJi5wOgQqJOPHKEFKNCBfhBC73','tzzVYLjxhBXgYCR4iOyp85VwNAL8y1K8zz7aumbSRo5PO')
# (consumer_key, consumer_secret, access_token, access_token_secret
# )
# this is thing that the tweeter api uses to verify our account in tweeter go where you created your acct and clic in details 'keys and token' so have to copy the consummer Api keys paste it inside the bracket btw quote similarly paste the consumer secret keys and then the access token and the access token secret

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)