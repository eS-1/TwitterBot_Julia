import random


def draw_fortune():
    '''
    おみくじ機能
    '''
    deck = ["大吉", "中吉", "小吉", "吉", "末吉"]
    return random.choice(deck)
