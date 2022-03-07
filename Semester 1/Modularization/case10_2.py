def pangram_check(sentence):
    alphabets_lower = "abcdefghijklmnopqrstuvwxyz"
    state = False
    for i in alphabets_lower:
            if i not in sentence.lower():
                state = False
            else:
                state = True
    if state == True:
        print('"'+sentence+'"'+" is a pangram")
    elif state == False:
        print('"'+sentence+'"'+" is not a pangram")

pangram_check("The quick brown fox jumps over the lazy dog")
pangram_check("Hello world")
pangram_check("By Jove, my quick study of lexicography won a prize!")
pangram_check("This is a sunny day")

#Jesus Christ if only I knew about smth.lower() sooner...

