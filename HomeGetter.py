from config import myAPI


if __name__ == "__main__":
    for status in myAPI.home_timeline():
        print("*************************************************************")
        print(status.user.name + " @" + status.user.screen_name)
        print(status.text)
