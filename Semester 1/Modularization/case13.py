alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
consonant = 'bcdfghjklmnpqrstwxyz'

def make_forming(verb):
    verbb = list(verb)
    if verbb[-1]=='e':
        if verb.endswith('ee') or verb.endswith('ye'):
            verbb.append('ing')
            for i in verbb:
                print(i, end='')
            print('')
        elif verb.endswith('ie'):
            verbb.pop(-1)
            verbb.pop(-1)
            verbb.append('ying')
            for i in verbb:
                print(i, end='')
            print('')
        elif verb == 'be':
            verbb.append('ing')
            for i in verbb:
                print(i, end='')
            print('')
        else:
            verbb.pop(-1)
            verbb.append('ing')
            for i in verbb:
                print(i, end='')
            print('')
    elif verbb[-2] not in consonant:
        for i in alphabets:
            if verbb[-1] == i:
                verbb.append(i)
                verbb.append('ing')
                for j in verbb:
                    print(j, end='')
                print('')
    elif verb.endswith('ie'):
        verbb.pop(-1)
        verbb.pop(-1)
        verbb.append('ying')
        for i in verbb:
            print(i, end='')
        print('')
    else:
        verbb.append('ing')
        for i in verbb:
            print(i, end='')
        print('')

make_forming('lie')
make_forming('see')
make_forming('move')
make_forming('hug')
make_forming('be')
make_forming('eye')
make_forming('grab')
make_forming('believe')

#some verbs may still display grammatical errors due to program limitations.