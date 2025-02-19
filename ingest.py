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
    "in",
    "return"
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
                token_type = "keyword" if buffer in KEYWORDS_MAP else "identifier"
                tokens.append(("word", buffer, token_type))
                buffer = ""
            
            if sign != "space":
                tokens.append(("special", char, CHARACTER_MAP[char]))
    
    if buffer:
        token_type = "keyword" if buffer in KEYWORDS_MAP else "identifier"
        tokens.append(("word", buffer, token_type))
    return tokens

def ingest(source_code):    
    lines = {}
    for line_num, line in enumerate(source_code.split("\n"), start=1):
        lines[line_num] = chew(line)
    return lines   

def digest(code):
    for row, line in code.items():
        print(f"\nLine {row}:")
        for token in line:
            if token[0] == "word":
                _, word, word_type = token
                print(f"{word_type}: {word}")
            else:
                _, char, char_type = token
                print(f"special ({char_type}): {char}")

# Test code
f = open("ingest.py", "r")
content = f.read()
code = ingest(content)

digest(code)