#class to represent node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def heap_max(node):
    if not node:
        return True
    
    if node.left:
        if node.key < node.left.key:
            return False
    if node.right:
        if node.key < node.right.key:
            return False
    
    return heap_max(no.left) and heap_max(no.right)

def complete_tree(no, index, node_number):
    if node is None:
        return True
    
    if index >= node_number:
        return False
    
    return (complete_tree(no.left, 2 * index + 1, node_number) and
            complete_tree(no.right, 2 * index + 2, node_number))

def count_node(node):
    if node is None:
        return 0
    return 1 + count_node(node.left) + count_node(node.right)

def heap(node):
    node_nummber = count_node(node)
    if complete_tree(node, 0, node_number) and heap_max(node):
        return True
    return False
