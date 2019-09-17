from config import myAPI
from datetime import datetime
import random


texts = ["ひゃくまんぱわー", "バカP...", "子猫ちゃん"]


def TweetAsBot():
    tweet = random.choice(texts) + " at "
    tweet += datetime.now().strftime('%X')
    myAPI.update_status(tweet)


if __name__ == "__main__":
    TweetAsBot()
