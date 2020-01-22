import random
import tweepy
from config import myAPI
from FollowBack import followBack


def tweetAsBot():
    texts = []
    with open("tweetTexts.txt", encoding="UTF-8") as f:
        texts = [s.strip() for s in f.readlines()]

    i = 0
    text = random.choice(texts)
    tweet = text + "(" + str(i) + ")"

    while i < 100:
        try:
            myAPI.update_status(tweet)
        except tweepy.TweepError:
            i += 1
            tweet = text + "(" + str(i) + ")"
        else:
            break


if __name__ == "__main__":
    tweetAsBot()

    followBack()
