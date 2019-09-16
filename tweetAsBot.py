from config import myAPI
import random


texts = ["ひゃくまんぱわー", "バカP...", "子猫ちゃん"]


def TweetAsBot():
    tweet = random.choice(texts)
    myAPI.update_status(tweet)


if __name__ == "__main__":
    TweetAsBot()
