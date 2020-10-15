alphabets_lower = "abcdefghijklmnopqrstuvwxyz"
alphabets_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = list(zip(alphabets_upper, alphabets_lower))

def pangram_check(sentence):
    alphabets_check = []
    for a in sentence:
        for b in alphabets_lower:
            if a in b:
                alphabets_check.append(a)
                break
        for c in alphabets_upper:
            if a in c:
                alphabets_check.append(a)
                break
    alphabets_2 = []
    for d in alphabets_check:
        for e in total:
            for f in e:
                if len(alphabets_2) == 0:
                    alphabets_2.append(d)
                elif len(alphabets_2) != 0:
                    for g in alphabets_2:
                        if d == g:
                            pass
                        elif d != f:
                            alphabets_2.append(d)
                            break
                break
            break
    final_alphabets = list(dict.fromkeys(alphabets_2)) #I got this code to remove duplicates from a list from careerkarma.com cuz my brain oh my godddddd
    for z in final_alphabets:
        final_length = len(final_alphabets)
        if z in alphabets_upper:
            final_length = len(final_alphabets)-1
            break
    if final_length == len(alphabets_lower) or final_length == len(alphabets_lower)-1 or final_length == len(alphabets_lower)-2 :
        print('"'+sentence+'"'+' is a pangram')
    else:
        print('"'+sentence+'"'+' is not a pangram')
pangram_check("The quick brown fox jumps over the lazy dog")
pangram_check("the quick brown fox jumps over the lazy dog")
pangram_check("Hello world")
pangram_check("This is a sunny day")
pangram_check("Mr. Jock, TV quiz PhD., bags few lynx")
pangram_check("GQ's oft lucky whiz Dr. J, ex-NBA MVP")
pangram_check("Jock nymphs waqf drug vex blitz")
pangram_check("Sphinx of black quartz, judge my vow.")
pangram_check("A wizard's job is to vex chumps quickly in fog")
pangram_check("Au ah astaga susah banget")
pangram_check("By Jove, my quick study of lexicography won a prize!")
pangram_check("Waxy and quivering, jocks fumble the pizza.")

#This is not a perfect program, it may give a false statement for your own-created pangram. Forgive me, I cannot fix it. This has caused my last brain cell to pop out into the void.