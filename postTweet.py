from config import myAPI


def PostTweet():
    print("内容を入力してください")
    tweet = input('>> ')
    print("\n")

    myAPI.update_status(tweet)


if __name__ == "__main__":
    while True:
        PostTweet()
        q = input("end(e)\ncontinue(Enter)\n")
        if q == "e":
            break
