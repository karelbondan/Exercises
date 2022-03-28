# made by karel bondan - 2440032373
import re
import string

# for windows, idk for other OS cause i dont use them. i had a stroke using kali linux
filename = __file__[__file__.rfind('\\'):].replace('\\', '')


# token class
class TokenClass:
    operators = ['-', '+', '/', '*', '.', '<=', '>=', '<', '>']
    openings = {'{': 'curly_bracket_opening',
                '[': 'bracket_opening',
                '(': 'parantheses_opening',
                '<?php': 'php_opening_tag', }
    closings = {'}': 'curly_bracket_closing',
                ']': 'bracket_closing',
                ')': 'parantheses_closing',
                '?>': 'php_closing_tag'}
    keywords = ['if', 'else', 'for', 'while', 'break', 'echo', 'function', 'class']
    assignment = "="
    variable = '$'
    end_token = ';'
    quote = ["\"", "'"]
    spaces = ['\t', ' ']
    breaks = '\n'


# array to append the analyzed tokens
analyzed = []


# check function to check the token class
def check(file):
    if file in TokenClass.operators:
        return 'math_operator'
    elif file in TokenClass.openings:
        return TokenClass.openings[file]
    elif file in TokenClass.closings:
        return TokenClass.closings[file]
    elif file in TokenClass.keywords:
        return 'keyword'
    elif file in TokenClass.assignment:
        return 'assignment'
    elif file in TokenClass.quote:
        return 'quote'
    elif file in TokenClass.variable:
        return 'variable'
    elif file in TokenClass.end_token:
        return 'end_token'
    elif file in TokenClass.spaces:
        return 'space'
    elif file in string.digits:
        return 'number'
    else:
        return 'unknown'


# main parser function (still has a ton of bugs, string literal is pain)
def parser(file):
    # checkers and a var for string literal
    quote = False
    quote_type = None
    str_literal = ''
    # outer loop, determining the current line number and the whole sentence
    for line, everything in enumerate(file.split('\n')):
        # index var for the column number
        dupe_index = 0
        # inner loop, for more detailed stuff about the sentences
        for column, inner in enumerate(everything.split()):
            # another checker for string literal
            spacebreak = True
            # for checking the token class
            cek = check(inner)
            # if the token class is unknown it means that it needs to be broken down further
            if cek == 'unknown':
                # var for determining identifiers
                first = ''
                current = ''
                # inner loop of the inner loop, for checking each letter of the sentence
                for index, detailed in enumerate(inner):
                    # string concat
                    if detailed in '.' and inner[index - 1] in TokenClass.quote:
                        # add string concatenation to array
                        dupe_index = everything.index(detailed, dupe_index)
                        analyzed.append([line + 1, dupe_index + 1, 'string_concat', detailed])
                    # string multiply
                    elif detailed in '*' and inner[index - 1] in TokenClass.quote:
                        # add string multipllication to array
                        dupe_index = everything.index(detailed, dupe_index)
                        analyzed.append([line + 1, dupe_index, 'string_multiply', detailed])
                    # string literal
                    elif quote:
                        # check again because why not
                        detailed_cek = check(detailed)
                        # this is the most complicated part, determining the space break if the sentence
                        # has changed index inside the previous inner loop. because it is splitted by space break,
                        # space break will be gone and therefore somehow will have to be re-added again. this is the
                        # usage of that spacebreak var declared earlier, hence why it is always True whenever the
                        # loop has begin again.
                        if spacebreak:
                            # add space then the next character
                            str_literal += f' {detailed}'
                            spacebreak = False
                        else:
                            # if not space break then just add the next character
                            str_literal += detailed
                        # if the check earlier is a quote class then it means it's either a new single/double qm or
                        # the end of the string.
                        if detailed_cek == 'quote':
                            if quote and quote_type == detailed:
                                # if end of string then replace space with &nbsp and ' with \'
                                str_ltl_final = str_literal.replace(' ', '&nbsp').replace("\'", "\\'")
                                # append it to the main analyzed array
                                analyzed.append(
                                    [line + 1, everything.index(str_literal) + 1, 'string_literal', str_ltl_final])
                                # set everything to default values to be reused in the future
                                quote = False
                                quote_type = None
                                str_literal = ''
                    # else if the token class is not unknown do things below
                    else:
                        # check again because why not (2)
                        detailed_cek = check(detailed)
                        if detailed_cek != 'unknown':
                            # if the class is not unknown and the class is quote then execute below statement. the
                            # first time the loop will detech a string literal beginning is trough this if statement
                            # below, hence that's why it's declared here, not above.
                            if detailed_cek == 'quote':
                                # if quote is currently true (in a string literal loop) and it has reached the end
                                # of the string then set everything to default values
                                if quote and quote_type == detailed:
                                    quote = False
                                    quote_type = None
                                else:
                                    # else if it is False and the quote type is None (currently not in a string
                                    # literal loop) then set these things.
                                    if quote_type is None:
                                        quote = True
                                        quote_type = detailed
                                        spacebreak = False
                                        str_literal += detailed
                            else:
                                # else if it is not string literal then just check what the token class is
                                # and add it to the main analyzed array
                                dupe_index = everything.index(detailed, dupe_index)
                                analyzed.append([line + 1, dupe_index + 1, detailed_cek, detailed])
                        # this whole else statement below is just for determining an identifier, it's pretty self
                        # explanatory
                        else:
                            if not first:
                                first = detailed
                            current += detailed
                            try:
                                nextt = inner[index + 1]
                            except IndexError:
                                nextt = ' '
                            if check(nextt) != 'unknown':
                                analyzed.append(
                                    [line + 1, everything.index(current) + 1, 'identifier', current])
                                first = current = ''
            # else if the class type is not unknown then just add it to the main analyzed array
            else:
                analyzed.append([line + 1, everything.index(inner) + 1, cek, inner])


# the source code, currently working as intended e x c e p t  ｓｔｒｉｎｇ　ｌｉｔｅｒａｌｓ　よけヶ, the one and only.
# it will break miserably if a spacebreak is to be added somewhere in there. pls spare me.
source_code = """<?php
class MyClass {
    function abc() { $i=5;
    $z=$i*2;
    echo "One '$=".$z;}
}
?>
"""

# call the function and print the items of analyzed array. no error handling atm cause i have a stroke already
# dealing with, once again, ｓｔｒｉｎｇ　ｌｉｔｅｒａｌｓ　よけヶ
parser(file=source_code)
for i in analyzed:
    print(i)
