def filter_long_words(lwords, n):
    words_final = []
    for i in lwords:
        word_length = len(i)
        if word_length>n:
            words_final.append(i)
        else:
            pass
    print(words_final)

filter_long_words(['amazing', 'wonderful', 'nice'], 5)
filter_long_words(['mempertanggungjawabkan', 'oh', 'hi'], 4)
filter_long_words(['dikarenakan', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch'], 20)