import random
import tweepy
from config import myAPI
from FollowBack import FollowBack


def TweetAsBot():
    texts = []
    with open("tweetTexts.txt", encoding="UTF-8") as f:
        texts = [s.strip() for s in f.readlines()]

    tweet = random.choice(texts)

    i = 0
    while i < 5:
        try:
            myAPI.update_status(tweet)
        except tweepy.TweepError:
            tweet = random.choice(texts)
            i += 1
        else:
            break


if __name__ == "__main__":
    TweetAsBot()

    FollowBack()
