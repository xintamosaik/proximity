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
    '+': "plus",
    '-': "minus",
    '!': "bang",
    '\\': "backslash",
}

KEYWORDS_MAP = [
    "for",
    "if",
    "else",
    "def",
]

def taste(character):
    if character.isalpha():
        return "alpha"
    if character.isnumeric():
        return "number"
    if character.isspace():
        return "space"
    return CHARACTER_MAP[character]

def chew(line):
    tokens = []
    buffer = ""
    
    for char in line:
        sign = taste(char)
        if sign in {"alpha", "number", "underscore"}:
            buffer += char
        else:
            if buffer:
                tokens.append(("word", buffer))
                buffer = ""
            
            if sign != "space":
                tokens.append(("special", char))
    if buffer:
        tokens.append(("word",buffer))
    return tokens

def ingest(source_code):    
    lines = {}
    for line_num, line in enumerate(source_code.split("\n"), start=1):
        lines[line_num] =  chew(line)
    return lines   


def digest(code):
    for row, line in code.items():
        
        for parts in line:
            if (parts[0] == "word"):
                word = parts[1]
                if word in KEYWORDS_MAP:
                    print ("keyword", word)
                else:
                    print("identifier", word)



f = open("ingest.py", "r")
content = f.read()

code = ingest(content)
digest(code)

