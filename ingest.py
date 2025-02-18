CHARACTER_MAP = {
    '(': "bracket_round_left",
    ')': "bracket_round_right",
    '{': "bracket_curly_left",
    '}': "bracket_curly_right",
    '[': "bracket_square_left",
    ']': "bracket_square_right",
    '>': "bigger_then",
    '<': "smaller_then",
    ',': "comma",
    '.': "dot",
    '"': "quote_double",
    "'": "quote_single",
    '=': "equal",
    '#': "hashtag",
    '_': "underscore",
    ':': "colon",
    '\\': "backslash",
}

def taste(character):
    if character.isalpha():
        return "alpha"
    if character.isnumeric():
        return "number"
    if character.isspace():
        return "space"
    return CHARACTER_MAP[character]
    
def chew(line):
    signs = {}
    for c in line:
        signs[c] = taste(c)

    tokens = [] # holds all the tokens of the line

    current = '' # holds the characters until a new token begins
    previousSign = '' # holds the 

    for char, sign in signs.items():
        print(char, sign)
        print(sign)
        print(type(sign))
        if sign == "space":
            print("is space")

def ingest(source_code):    
    lines = {}
    for line_num, line in enumerate(source_code.split("\n"), start=1):
        lines[line_num] = {line}    
        chew(line)
    # print(lines)

f = open("ingest.py", "r")
content = f.read()
content = "exampe = 42"
ingest(content)
