import re
import MeCab
import random
from collections import deque


def gen_sentence(some_texts):
    sentences = re.findall(".*?[。？♪！]", some_texts)
    for sentence in sentences:
        yield sentence


def wakati_word(text):
    tagger = MeCab.Tagger("-Owakati")
    parsed_text = ""
    for generated_text in gen_sentence(text):
        parsed_text += " "
        parsed_text += tagger.parse(generated_text)
    # print(parsed_text)
    word_list = parsed_text.replace("\n", "").split(" ")
    word_list = [word for word in word_list if word != ""]
    # print(word_list)
    return word_list


def make_model(text, order=2):
    model = {}
    word_list = wakati_word(text)
    queue = deque([], order)
    queue.append("[BOS]")
    for word in word_list:
        if len(queue) == order:
            if queue[-1] == "。" or queue[-1] == "？" or \
               queue[-1] == "♪" or queue[-1] == "！":
                markov_key = tuple(queue)
                if markov_key not in model:
                    model[markov_key] = []
                model[markov_key].append("[BOS]")
                queue.append("[BOS]")
            markov_key = tuple(queue)
            if markov_key not in model:
                model[markov_key] = []
            model[markov_key].append(word)
        queue.append(word)
    return model


def make_markov_sentence(model, order=2, sentence_num=10, max_words=140, seed="[BOS]"):
    make_count = 0
    key_candidates = [key for key in model if key[0] == seed]
    if not key_candidates:
        print("Can't find keyword.")
        return
    markov_key = random.choice(key_candidates)
    queue = deque(list(markov_key), order)

    sentence = "".join(markov_key)
    for i in range(max_words):
        markov_key = tuple(queue)
        next_word = random.choice(model[markov_key])
        sentence += next_word
        queue.append(next_word)
        if next_word == "。" or next_word == "？" or \
           next_word == "♪" or next_word == "！":
            make_count += 1
            if make_count >= sentence_num:
                break
    return sentence


if __name__ == "__main__":
    data = ""
    with open("tweetTexts.txt", encoding="UTF-8") as f:
        for i in f.read().splitlines():
            data += i
    # print(data)
    word_model = make_model(data, order=2)
    sentence = make_markov_sentence(word_model, order=2, sentence_num=1)
    # print(word_model)
    print(sentence.replace("[BOS]", ""))
