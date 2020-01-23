from config import myAPI

if __name__ == "__main__":
    timeline = myAPI.mentions_timeline(count=5)

    for mention in timeline:
        print(mention.text)
        print(mention.favorited)
