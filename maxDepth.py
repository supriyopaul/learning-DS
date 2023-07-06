from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root: return depth
        q = deque([root])
        while q:
            level_nodes = []
            level_length = len(q)
            for _ in range(level_length):
                curr_root = q.popleft()
                level_nodes.append(curr_root.val)
                if curr_root.left is not None:
                    q.append(curr_root.left)
                if curr_root.right is not None:
                    q.append(curr_root.right)
            depth += 1
        return depth


if __name__ == "__main__":
   # [3,9,20,null,null,15,7]
   t = TreeNode(val=TreeNode(3), left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
   print(Solution().maxDepth(t))