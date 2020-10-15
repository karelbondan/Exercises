def make_forms(verb):
    verbb = list(verb)
    if verb.endswith('y'):
        verbb.pop(-1)
        verbb.append('ies')
        for i in verbb:
            print(i, end='')
        print('')
    elif verb.endswith('sh') or verb.endswith('ch'):
        verbb.append('es')
        for i in verbb:
            print(i, end='')
        print('')
    elif verb.endswith('o') or verb.endswith('z') or verb.endswith('x'):
        verbb.append('es')
        for i in verbb:
            print(i, end='')
        print('')
    else:
        verbb.append('s')
        for i in verbb:
            print(i, end='')
        print('')


make_forms('try')
make_forms('brush')
make_forms('run')
make_forms('fix')