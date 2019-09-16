import tweepy


CONSUMER_KEY = "1p2nL1mgjepZhrWKztVlUMzQU"
CONSUMER_SECRET = "2aFBb7ZeHaNBr8V63rkk3tKgAoq9RsLmfSc67T6c6GYqoCt81u"
ACCESS_TOKEN = "1118307764361555968-FTROMCYZh1UhXaFR9wcWGAIsWWYVrp"
ACCESS_TOKEN_SECRET = "W5ypcfOmg1T7FKLxPLpxkabv1ozaqudqBt4nYqeTR2Ee7"

CK = CONSUMER_KEY
CS = CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET

authHandle = tweepy.OAuthHandler(CK, CS)
authHandle.set_access_token(AT, ATS)
myAPI = tweepy.API(authHandle)
