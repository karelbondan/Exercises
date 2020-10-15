def letter_count(words):
    letter = list(map(str, words))
    let_count = []
    for i in letter:
        count = len(i)
        let_count.append(count)
        final = dict(zip(letter, let_count))
    print(final)

letter_count(['how', 'are', 'you'])
letter_count(['good', 'morning', 'guys'])
letter_count(['the', 'sun', 'is', 'shining', 'brightly', 'today'])