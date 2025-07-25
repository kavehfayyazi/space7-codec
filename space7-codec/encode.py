import os
from collections import Counter, deque
from tree import TreeNode
from utils.codec_utils import convert_char_to_encoding
from utils.file_utils import get_string_from_file, write_string_to_file
from utils.tree_utils import get_val, deque_insert, get_mapping

def encode_freq_tree(elem, text=''):
    if elem is None:
        return
    elif type(elem) is TreeNode:
        text += ' '
        text = encode_freq_tree(elem.left, text)
        text = encode_freq_tree(elem.right, text)
    else: #tree = (char, count)
        text += '7' + convert_char_to_encoding(elem[0])
    return text

def encode(message, encoded_name):
    ctr = Counter(message)
    de = deque()
    for char, count in ctr.most_common():
        de.append((char, count))
    while len(de) > 1:
        right = de.pop()
        left = de.pop()
        node = TreeNode(get_val(left) + get_val(right))
        node.add_left(left)
        node.add_right(right)
        deque_insert(de, node)

    freq_tree = encode_freq_tree(de[0])
    mapping = get_mapping(de[0])

    encoded_message = ''.join(mapping[char] for char in message)
    full_content = freq_tree + encoded_message
    write_string_to_file(encoded_name, full_content)

def main(file_name, encoded_name):
    message = get_string_from_file(file_name)
    encode(message, encoded_name)