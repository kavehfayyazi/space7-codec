def convert_char_to_encoding(c):
    binary = format(ord(c), '08b')
    return ''.join('7' if c == '1' else ' ' for c in binary)

def convert_encoding_to_char(en):
    binary = "".join('1' if c == '7' else '0' for c in en)
    char = int(binary, 2)
    return chr(char)

def is_tree(char):
    return True if char == ' ' else False