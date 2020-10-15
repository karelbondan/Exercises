def find_longest_word(lwords):
    words_count = []
    for i in lwords:
        k = 0
        for j in lwords:
            word_final = []
            length = []
            count = len(j)
            if count>k:
                k = count
                word_final.append(j)
                length.append(count)
                final = dict(zip(word_final, length))
            else:
                pass
    print(final)

find_longest_word(['hi', 'wonderland', 'hello', 'welcome'])
find_longest_word(['handsome', 'beautiful', 'amazing'])
find_longest_word(['mempertanggungjawabkan', 'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch', 'pneumonoultramicroscopicsilicovolcanoconiosis'])