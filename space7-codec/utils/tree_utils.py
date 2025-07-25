from collections import defaultdict, deque
from tree import TreeNode

def get_val(elem):
    return elem.data if type(elem) is TreeNode else elem[1]

# inserting a (char,  count) or a treenode
def deque_insert(de, elem):
    temp = deque()
    added = False
    while de:
        rear = de.pop()
        if get_val(rear) >= get_val(elem):
            de.append(rear)
            de.append(elem)
            added = True
            break
        else:
            temp.appendleft(rear)
    if added == False:
        de.append(elem)
    while temp:
        de.append(temp.pop())

def get_mapping(elem, prefix='', dict=defaultdict()):
    if elem is None:
        return
    elif type(elem) is TreeNode:
        get_mapping(elem.left, ''.join((prefix,' ')), dict)
        get_mapping(elem.right, ''.join((prefix,'7')), dict)
    else: # elem = (char, count)
        dict[elem[0]] = prefix
    return dict

def is_tree(char):
    return True if char == ' ' else False