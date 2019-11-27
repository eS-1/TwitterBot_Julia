from config import myAPI

MY_ID = "k3bot_Julia"


def ReplyAsBot():
    timeline = myAPI.mentions_timeline(count=5)

    for status in timeline:
        screen_name = status.author.screen_name.encode("UTF-8")
        user_name = status.author.name
        scname_str = screen_name.decode()
        text = status.text
        print("------------------------------")
        print(user_name)
        print(text)
        print("------------------------------")

        reply_text = "@" + scname_str + " "

        if "おはよう" in text:
            reply_text += "おはよう、" + user_name + "P！"
        else:
            reply_text += "test"

        if str(status.in_reply_to_screen_name) == MY_ID and str(status.user.screen_name) != MY_ID:
            myAPI.update_status(status=reply_text,
                                in_reply_to_status_id=status.id)
        else:
            print("Error.")


if __name__ == "__main__":
    ReplyAsBot()
