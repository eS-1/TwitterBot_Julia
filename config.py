import tweepy

consumer_key = "1p2nL1mgjepZhrWKztVlUMzQU"
consumer_secret = "2aFBb7ZeHaNBr8V63rkk3tKgAoq9RsLmfSc67T6c6GYqoCt81u"
access_token_key = "1118307764361555968-FTROMCYZh1UhXaFR9wcWGAIsWWYVrp"
access_token_secret = "W5ypcfOmg1T7FKLxPLpxkabv1ozaqudqBt4nYqeTR2Ee7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

myAPI = tweepy.API(auth)
