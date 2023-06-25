from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
   # [3,9,20,null,null,15,7]
   t = TreeNode(val=TreeNode(3), left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
   print(Solution().maxDepth(t))