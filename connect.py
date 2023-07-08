from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque([root])
        
        while q:
            level_length = len(q)
            level_nodes = []
            for _ in range(level_length):
                if q:
                    curr_node = q.popleft()
                    level_nodes.append(curr_node)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            for index, node in enumerate(level_nodes):
                try:
                    node.next = level_nodes[index+1]
                except IndexError:
                    node.next = None
            
            
        return root


if __name__ == '__main__':
    root = Node(1) # root = [1,2,3,4,5,6,7]
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(Solution().connect(root)) # [1,#,2,3,#,4,5,6,7,#]