"""i don't use string.punctuation because there's a single quote, in it, which can be problematic with words that use it (ex: don't).
And there are more things that doesn't exist in string.punctuations such as left and right double quotation marks.
n.b. This solution may not be accurate."""
import string

punctuation = '!"#$%&()*+,-—./:;<=>?@[\]^_`{|}~’“”‘'
file = open('callofthewild.txt', 'r', encoding='utf8')
def hapax_legomenon(file):
    word_count = {}
    new_words = []
    wordlist = file.read()
    for impostor in punctuation:
        if impostor in wordlist:
            wordlist = wordlist.replace(impostor, ' ')
        else: pass
    for impostor2 in string.digits:
        if impostor2 in wordlist:
            wordlist = wordlist.replace(impostor2, ' ')
        else: pass
    for items in wordlist.lower().split():
        for ah in items.split(' '):
            word_count.setdefault(ah, 0)
            word_count[ah] = word_count[ah] + 1
    for words in word_count:
        if word_count[words] == 1:
            new_words.append(words)
        else: pass
    print("\nTotal words count: " + str(len(word_count)))
    print("Hapax Legomena count: " + str(len(new_words)))
    print("Hapax Legomena percentage: " + str(round((len(new_words) / len(word_count) * 100), 2)) + "%")
    print("\nThe words are:")
    for contents in new_words:
        print(contents)

hapax_legomenon(file)