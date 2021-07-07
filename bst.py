class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
tree.insert(80)
print(tree.lookup(20))
print(tree.lookup(80))
print(tree.lookup(1))

