import random


def draw_fortune():
    '''
    おみくじ機能
    '''
    result = "どれどれ、結果は..."
    deck = ["大吉",
            "中吉",
            "小吉",
            "吉",
            "末吉"]
    result += random.choice(deck) + "だ。ついでに1曲聴いてくか？"
    return result


if __name__ == "__main__":
    print(draw_fortune())
