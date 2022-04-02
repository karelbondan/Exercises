# made by karel bondan - 2440032373
import re
import string


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


# for positioning (line and column)
class Position:
    def __init__(self, line, column, index):
        self.line = line
        self.column = column
        self.index = index  # for the entirety of the code

    def advance(self, char):
        self.column += 1
        self.index += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        return self

    # for determining the start position of, example, an identifier
    def copy(self):
        return Position(self.line, self.column, self.index)


# parent error class
class Error:
    def __init__(self, line, col, error_type, error_message, filename):
        self.line = line
        self.col = col
        self.err_type = error_type
        self.err_msg = error_message
        self.filename = filename

    def to_string(self):
        return f'{self.err_type}: {self.err_msg}\nFile {self.filename}, line {self.line}: col {self.col}'


# children of error class
class PHPErr(Error):
    def __init__(self, line, col, error_message, filename):
        super(PHPErr, self).__init__(line, col, 'InvalidCodeError', error_message, filename)


class EOFErr(Error):
    def __init__(self, line, col, error_message, filename):
        super(EOFErr, self).__init__(line, col, 'EOFError', error_message, filename)


class InvalidSequenceErr(Error):
    def __init__(self, line, col, error_message, filename):
        super(InvalidSequenceErr, self).__init__(line, col, 'InvalidSequenceError', error_message, filename)


class IllegalCharErr(Error):
    def __init__(self, line, col, error_message, filename):
        super(IllegalCharErr, self).__init__(line, col, 'IllegalCharacterError', error_message, filename)


# for token categorization
class Token:
    def __init__(self, line, col, token_type, token_value=None):
        self.line = line
        self.col = col
        self.token_type = token_type
        self.token_val = token_value

    def format(self):
        if self.token_val:
            return [self.line, self.col, self.token_type, self.token_val]
        else:
            return [self.line, self.col, self.token_type]


# for lexical analysis
class Lexer:
    def __init__(self, text, filename):
        self.text = text
        self.pos = Position(1, 0, -1)
        self.current_char = None
        self.filename = filename
        self.advance()

    # advancing the position of the current pointer
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    # tokenize method
    def tokenizer(self):
        analyzed_tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t\n':
                self.advance()
            elif not analyzed_tokens:
                res = self.check_php_open()
                if isinstance(res, Error):
                    return [], res
                else:
                    analyzed_tokens.append(res)
            elif self.current_char in TokenClass.operators:
                if self.current_char == '/' and self.text[self.pos.index + 1] == '/':
                    res = self.comment()
                    if isinstance(res, Error):
                        return [], res
                else:
                    analyzed_tokens.append(
                        Token(self.pos.line, self.pos.column, 'math_operator', self.current_char).format())
                    self.advance()
            elif self.current_char in TokenClass.openings:
                analyzed_tokens.append(
                    Token(self.pos.line, self.pos.column, TokenClass.openings[self.current_char]).format())
                self.advance()
            elif self.current_char in TokenClass.closings:
                analyzed_tokens.append(
                    Token(self.pos.line, self.pos.column, TokenClass.closings[self.current_char]).format())
                self.advance()
            elif self.current_char in string.digits:
                analyzed_tokens.append(self.make_number())
            elif self.current_char in string.digits + string.ascii_letters + '_':
                res = self.make_identifier()
                if isinstance(res, Error):
                    return [], res
                else:
                    analyzed_tokens.append(res)
            elif self.current_char in TokenClass.quote:
                res = self.make_string()
                if isinstance(res, Error):
                    return [], res
                else:
                    analyzed_tokens.append(res)
            elif self.current_char in TokenClass.assignment:
                analyzed_tokens.append(Token(self.pos.line, self.pos.column, 'assignment').format())
                self.advance()
            elif self.current_char in TokenClass.variable:
                analyzed_tokens.append(Token(self.pos.line, self.pos.column, 'variable').format())
                self.advance()
            elif self.current_char in TokenClass.end_token:
                analyzed_tokens.append(Token(self.pos.line, self.pos.column, 'end_token').format())
                self.advance()
            elif self.current_char == "#":
                self.comment()
            elif self.current_char + self.text[self.pos.index + 1] == '?>':
                analyzed_tokens.append(Token(self.pos.line, self.pos.column, 'php_closing_tag').format())
                self.advance()
                self.advance()
            else:
                return [], IllegalCharErr(self.pos.line, self.pos.column, f"Illegal Character '{self.current_char}'",
                                          self.filename)

        if analyzed_tokens[-1][-1] != 'php_closing_tag':
            return [], PHPErr(self.pos.line, self.pos.column, "Invalid PHP Closing Tag (Not detected or mistyped)",
                              self.filename)

        return analyzed_tokens, None

    def check_php_open(self):
        php_open = '<?php'
        php_check = ''
        start_pos = self.pos.copy()

        while self.current_char is not None:
            if self.current_char in ' \n':
                break
            php_check += self.current_char
            self.advance()
        if php_check.strip() != php_open:
            return PHPErr(start_pos.line, start_pos.column, "Invalid PHP Opening Tag (Not detected or mistyped)",
                          self.filename)
        else:
            return Token(start_pos.line, start_pos.column, 'php_opening_tag').format()

    def make_number(self):
        dot_count = 0
        num = ''
        start_pos = self.pos.copy()

        while self.current_char is not None and self.current_char in string.digits + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    self.advance()
                    break
                dot_count += 1
            num += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(start_pos.line, start_pos.column, 'integer', num).format()
        else:
            return Token(start_pos.line, start_pos.column, 'float', num).format()

    def make_identifier(self):
        identifier = ''
        start_pos = self.pos.copy()

        while self.current_char is not None and self.current_char in string.ascii_letters + string.digits + '_':
            identifier += self.current_char
            self.advance()

        if identifier in TokenClass.keywords:
            return Token(start_pos.line, start_pos.column, 'keyword', identifier).format()
        else:
            return Token(start_pos.line, start_pos.column, 'identifier', identifier).format()

    def make_string(self):
        str_full = ''
        is_escape = False

        escape_char = {'n': '\n', 't': '\t'}

        self.advance()  # to skip current char which is "
        while self.current_char != '"':
            if self.current_char is None:
                return EOFErr(self.pos.line, self.pos.column, 'String literal not ended properly', self.filename)

            elif is_escape:
                try:
                    str_full += escape_char[self.current_char]
                    is_escape = False
                except KeyError:
                    return InvalidSequenceErr(self.pos.line, self.pos.column,
                                              f'Not a valid escape character: {self.current_char}', self.filename)
            else:
                if self.current_char == '\\':
                    is_escape = True
                elif self.current_char == ' ':
                    str_full += '&nbsp'
                elif self.current_char == '\'':
                    str_full += "\\'"
                else:
                    str_full += self.current_char
            self.advance()

        self.advance()
        return Token(self.pos.line, self.pos.column, 'string_literal', str_full).format()

    def comment(self):
        start_pos = self.pos.copy()

        if self.current_char + self.text[self.pos.index + 1] == '//':
            # advance 2 times because it's checking for two indexes. thus skipping the //
            self.advance()
            self.advance()

            try:
                while self.current_char + self.text[self.pos.index + 1] != '//':
                    if self.current_char is None:
                        return EOFErr(start_pos.line, start_pos.column, 'Multiline comment not ended properly',
                                      self.filename)
                    else:
                        self.advance()
            except IndexError:
                return EOFErr(start_pos.line, start_pos.column, 'Multiline comment not ended properly', self.filename)

            # advance two times again to skip the multi-line comment closing //
            self.advance()
            self.advance()
        else:
            while self.current_char != '\n':
                self.advance()


# source code
source_code = """<?php
class MyClass {
    # this is a single-line comment
    // this is a multiline comment
    another comment on a new line
    //
    function abc(){ $i=5;
    $z=$i*2;
    echo "One '$=".$z;}
}
?>
"""

# getting the current file name
fn = __file__[__file__.rfind('/') + 1:]

# call the lexer class and tokenize the source code
lexer = Lexer(source_code, fn)
testing, error = lexer.tokenizer()

# print
if not error:
    for i in testing:
        print(i)
else:
    print(error.to_string())
