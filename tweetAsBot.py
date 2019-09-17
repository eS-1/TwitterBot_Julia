from config import myAPI
from datetime import datetime
from datetime import timedelta
import random


texts = ["ひゃくまんぱわー", "バカP...", "子猫ちゃん"]


def TweetAsBot():
    current = datetime.now() + timedelta(hours=9)
    tweet = random.choice(texts) + " at " + current.strftime('%Y-%m-%d %X')
    myAPI.update_status(tweet)


if __name__ == "__main__":
    TweetAsBot()
