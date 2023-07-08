from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) == 1: return root
        
        print(preorder, inorder)
        root_position_in_inorder = inorder.index(root_val)
        left_inorder = inorder[0:root_position_in_inorder]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_inorder = inorder[root_position_in_inorder+1::]
        right_preorder = preorder[1+len(left_inorder):]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(Solution().buildTree(preorder, inorder)) #[3,9,20,null,null,15,7]