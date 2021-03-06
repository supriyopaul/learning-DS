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

    def bfs_traverse(self):
        current_node = self.root
        q = deque([current_node])
        result = []
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left: q.append(current_node.left)
            if current_node.right: q.append(current_node.right)
            result.append(current_node.value)
        return result

    def bfs_traverse_recursive(self, q, result):
        if len(q) == 0: return result
        current_node = q.popleft()
        result.append(current_node.value)
        if current_node.left: q.append(current_node.left)
        if current_node.right: q.append(current_node.right)
        return self.bfs_traverse_recursive(q, result)

    def dfs_inorder(self):
        return [e.value for e in self._traverse_inorder(self.root, deque())]

    def _traverse_inorder(self, node, q):
        if node.left: self._traverse_inorder(node.left, q)
        q.append(node)
        if node.right: self._traverse_inorder(node.right, q)
        return q

    def dfs_preorder(self):
        return [e.value for e in self._traverse_preorder(self.root, deque())]

    def _traverse_preorder(self, node, q):
        q.append(node)
        if node.left: self._traverse_preorder(node.left, q)
        if node.right: self._traverse_preorder(node.right, q)
        return q

    def dfs_postorder(self):
        return [e.value for e in self._traverse_postorder(self.root, deque())]

    def _traverse_postorder(self, node, q):
        if node.left: self._traverse_postorder(node.left, q)
        if node.right: self._traverse_postorder(node.right, q)
        q.append(node)
        return q

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
print(tree.lookup(20))
print(tree.lookup(80))
print(tree.lookup(1))
print(tree.bfs_traverse())
print(tree.bfs_traverse_recursive(deque([tree.root]), []))
print(tree.dfs_inorder())
print(tree.dfs_preorder())
print(tree.dfs_postorder())
