def char_freq(str):
    char_count = dict((i, str.count(i)) for i in str)
    print(char_count)

char_freq('akjfklanfklewgl')
char_freq('sohard')
char_freq('lklklklklklklkkklkkkklkkkkkaaaaaaa')