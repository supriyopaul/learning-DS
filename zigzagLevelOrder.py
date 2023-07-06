from typing import Optional, List
from collections import deque

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque([root])
        result = []
        level = 0
        while q:
            level_length = len(q)
            level_nodes = []
            level = level + 1
            for _ in range(level_length):
                curr_node = q.popleft()
                level_nodes.append(curr_node.val)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            print(level, level_nodes)
            if level % 2 == 0: result.append(level_nodes[::-1])
            else: result.append(level_nodes)
            
        return(result)
                

if __name__ == "__main__":
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root)) # [3],[20,9],[15,7]]