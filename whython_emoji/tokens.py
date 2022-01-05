# *###################
# * IMPORTS
# *###################

from editable_.editable import KEYWORDS_DICT

# *###################
# * TOKENS
# * DON'T EDIT THESE!
# *###################

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_STRING = "STRING"

TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_EXPONENT = "EXPONENT"

TT_IDENTIFIER = "IDENTIFIER"
TT_KEYWORD = "KEYWORD"
TT_EQ = "EQ"

TT_EE = "EE"
TT_NE = "NE"
TT_LT = "LT"
TT_GT = "GT"
TT_LTE = "LTE"
TT_GTE = "GTE"

TT_COMMA = "COMMA"
TT_ARROW = "ARROW"
TT_NEWLINE = "NEWLINE"

TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_LSQUARE = "["
TT_RSQUARE = "]"

TT_EOF = "EOF"

KEYWORDS = []
for keyword_index in KEYWORDS_DICT:
    KEYWORDS.append(KEYWORDS_DICT[keyword_index])

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'