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
    signs = {c: taste(c) for c in line}

    tokens = []  # Holds all the tokens of the line
    buffer = ""  # Stores characters to form multi-character tokens
    previous_sign = None  # Tracks the previous character type

    for char, sign in signs.items():
        # If sign changes from alphanumeric to non-alphanumeric, store buffer
        if buffer and sign not in {"alpha", "number", "underscore"}:
            tokens.append(buffer)
            buffer = ""

        # If it's a symbol, store it as an individual token
        if sign not in {"alpha", "number", "underscore", "space"}:
            tokens.append(char)
        elif sign != "space":  # If it's not a space, add it to the buffer
            buffer += char

        previous_sign = sign

    # Append the last buffered token if it exists
    if buffer:
        tokens.append(buffer)

    print(tokens)  # Output for debugging

def ingest(source_code):    
    lines = {}
    for line_num, line in enumerate(source_code.split("\n"), start=1):
        lines[line_num] = {line}    
        chew(line)
    # print(lines)

f = open("ingest.py", "r")
content = f.read()
content = "example = 42"
ingest(content)
