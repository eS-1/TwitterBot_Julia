from config import myAPI
import tweepy
from datetime import datetime
from datetime import timedelta
import random


texts = ["ひゃくまんぱわー", "バカP...", "子猫ちゃん", "シズ、言ってやりな"]


def TweetAsBot():
    current = datetime.now() + timedelta(hours=9)
    tweet = random.choice(texts) + " in " + current.strftime('%Y-%m-%d %X')
    myAPI.update_status(tweet)


def GetAllFollowers():
    followers = list()
    for follower in tweepy.Cursor(myAPI.followers).items():
        followers.append(follower)
    return followers


def GetAllFriends():
    friends = list()
    for friend in tweepy.Cursor(myAPI.friends).items():
        friends.append(friend)
    return friends


if __name__ == "__main__":
    TweetAsBot()

    followers = GetAllFollowers()
    friends = GetAllFriends()
    for unknown in followers:
        if unknown not in friends:
            unknown.follow()
