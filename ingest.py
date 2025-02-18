def taste(character):
    if character.isalpha():
        return "alpha"
    if character.isnumeric():
        return "number"
    if character.isspace():
        return "space"
    if character == '(':
        return "bracket_round_left"
    if character == ')':
        return "bracket_round_right"
    if character == '{':
        return "bracket_curly_left"
    if character == '}':
        return "bracket_curly_right"
    if character == '[':
        return "bracket_square_left"
    if character == ']':
        return "bracket_square_right"
    if character == ',':
        return "comma"
    if character == '.':
        return "dot"
    if character == '"':
        return "quote_double"
    if character == "'":
        return "quote_single"
    if character == '=':
        return "equal"
    if character == '#':
        return "hashtag"
    if character == '_':
        return "underscore"
    if character == ':':
        return "colon"
    if character == '\\':
        return "backslash"
    
    
    
    print(character)
    
def chew(line):
    characters = {}
    current = ''
    currentToken = ''
    tokens = []

    for c in line:
        characters[c] = {taste(c)}

def ingest(source_code):    
    lines = {}
    for line_num, line in enumerate(source_code.split("\n"), start=1):
        lines[line_num] = {line}    
        chew(line)
    # print(lines)

f = open("ingest.py", "r")
content = f.read()
    
ingest(content)
