def word_frequencies(mylist):
    ah = mylist.split(sep=' ')
    word_count = {}
    for words in ah:
        word_count.setdefault(words, 0)
        word_count[words] = word_count[words] + 1
    return word_count

print(word_frequencies(input("Enter something: ")))