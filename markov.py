def two_gram(text):
    result = ""
    len_text = len(text)
    ch_second = list(range(1, len_text + 1))
    for i in range(len_text - 1):
        result += text[i] + text[ch_second[i]] + "\n"
    return result


if __name__ == "__main__":
    data = ""
    with open("tweetTexts.txt", encoding="UTF-8") as f:
        for i in f.read().splitlines():
            data += i
    grammed = two_gram(data)
    # print(data)
    print(grammed)
