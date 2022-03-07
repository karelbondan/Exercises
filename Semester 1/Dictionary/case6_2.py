import string
additional = ' '

def alphabet_rotation(rotation, sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotated_letters = ''
    rotated_letters_up = ''
    step = int(rotation)
    rotated_letters += letters[step:]
    rotated_letters_up += letters_up[step:]
    for i in letters:
        rotated_letters += i
        if len(rotated_letters)==26:
            break
    for j in letters_up:
        rotated_letters_up += j
        if len(rotated_letters_up)==26:
            break
    final_letters = letters+letters_up
    final_rotated_letters = rotated_letters+rotated_letters_up
    dicti = dict(zip(final_letters, final_rotated_letters))
    return encode_decode(dicti, sentence)

def encode_decode(dicti, usr_input):
    new_text = ''
    for item in usr_input:
        for values in dicti.keys():
            if item==values:
                new_text += dicti[item]
            if item in string.punctuation or item in string.digits or item in additional:
                new_text += item
                break
    return new_text

input_rot = int(input("Enter how many rotation you want (in int): "))
input_sen = input("Enter your phrase: ")
print("Rotation: "+str(input_rot))
print("Output: "+'"'+alphabet_rotation(input_rot, input_sen)+'"')