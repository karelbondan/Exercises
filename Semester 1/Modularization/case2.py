def translate(phrase):
    newphrase = ""
    for char in phrase:
        if char not in ('a','e','i','o','u',' '):
            newphrase += char + 'o' + char
        else:
            newphrase += char
    print (newphrase)

translate('this is fun')
translate('wow guys')
translate('this is amusingly ridiculous')