from collections import defaultdict
from utils.codec_utils import is_tree, convert_encoding_to_char
from utils.file_utils import get_string_from_file, write_string_to_file

def decode_freq_tree(text, dict, index=0, code=''): # 0 is a tree f/7 is a node
    if is_tree(text[index]):
        index = decode_freq_tree(text, dict, index+1, code + ' ')
        index = decode_freq_tree(text, dict, index, code + '7')
    else: #is a node
        dict[code] = convert_encoding_to_char(text[index+1:index+9])
        return index+9
    return index

def decode_message(text, index, dict):
    current = ''
    decoded_text = ''
    for char in text[index:]:
        current += char
        if current in dict: # maps to a character:
            decoded_text += dict[current]
            current = ''
    return decoded_text

def main(file_name, converted_name):
    content = get_string_from_file(file_name)
    dict = defaultdict(str)
    index = decode_freq_tree(content,dict)
    message = decode_message(content, index, dict)
    write_string_to_file(converted_name, message)