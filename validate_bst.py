from collections import deque

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        if not (self.left and self.right): return True
        return False


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def lookup(self, value):
        if not self.root: return False
        elif value == self.root: return True
        current_node = self.root
        while True:
            if value < current_node.value and current_node.left:
                current_node = current_node.left
            elif value > current_node.value and current_node.right:
                current_node = current_node.right
            elif value == current_node.value:
                return True
            elif not (current_node.left and current_node.right):
                return False

    def insert(self, value):
        node = Node(value)
        if not self.root: self.root = node; return
        current_node = self.root
        while True:
            print("value: {}, current_node: {}".format(value, current_node.value))
            if value < current_node.value and current_node.left:
                current_node = current_node.left
            elif value >= current_node.value and current_node.right:
                current_node = current_node.right
            elif value < current_node.value and not current_node.left:
                current_node.left = node
                print("value: {} put in left of {}".format(value, current_node.value))
                break
            elif value >= current_node.value and not current_node.right:
                current_node.right = node
                print("value: {} put in right of {}".format(value, current_node.value))
                break
        return

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(14)
tree.insert(1)

tree_str='''
     9\n
   /   \ \n
  4     20\n
 / \   /  \ \n
1   6 14   170\n
'''
print(tree_str)

def validate_bst(tree):
    root = tree.root
    nodes = bfs_traverse(root)
    return nodes

def bfs_traverse(node):
    q = deque([node])
    while len(q) > 0:
        node = q.popleft()
        if node.left:
            if node.left.value > node.value: return False
            q.append(node.left)
        if node.right:
            if node.right.value < node.value: return False
            q.append(node.right)
    return True

print(validate_bst(tree))
tree2 = BinarySearchTree()
tree2.root = Node(2)
tree2.root.left = Node(3)
tree2.root.right = Node(1)
print(validate_bst(tree2))

