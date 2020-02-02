import fortune
from config import myAPI

MY_ID = "k3bot_Julia"


def replyAsBot():
    '''
    リプライ用の関数。
    '''
    timeline = myAPI.mentions_timeline(count=20)

    for status in timeline:
        status_id = status.id
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
        elif "おやすみ" in text:
            reply_text += "おやすみ、" + user_name + "P。良い夢見ろよ？"
        elif "たすけて" in text:
            reply_text += "どうした" + user_name + "P、何があったのさ？"
        elif "つらい" in text:
            reply_text += "大丈夫か？アタシがついてる、心配すんな"
        elif "おみくじ" in text:
            reply_text += fortune.draw_fortune()
        else:
            reply_text += "test"

        if str(status.in_reply_to_screen_name) == MY_ID and str(status.user.screen_name) != MY_ID and (not status.favorited):
            myAPI.create_favorite(status_id)
            myAPI.update_status(status=reply_text,
                                in_reply_to_status_id=status.id)
        else:
            print("Error.")


if __name__ == "__main__":
    replyAsBot()
