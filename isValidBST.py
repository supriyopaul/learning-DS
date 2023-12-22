from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_tree = []
        
        def preorder_dfs(root):
            if root:
                preorder_dfs(root.left)
                inorder_tree.append(root.val)
                preorder_dfs(root.right)
        
        if root: preorder_dfs(root)
        if len(inorder_tree) == 1: return True
        right = len(inorder_tree) - 1
        left = right - 1
        while left >= 0:
            if inorder_tree[right] <= inorder_tree[left]: return False
            right -= 1
            left -= 1

        return True


if __name__ == "__main__":
    two = TreeNode(2)
    one = TreeNode(1)
    three = TreeNode(3)
    root = two
    root.left = one
    root.right = three
    print(Solution().isValidBST(root))
    five = TreeNode(5)
    four = TreeNode(4)
    six = TreeNode(6)
    root = five
    root.left = one
    root.right = four
    root.right.left = three
    root.right.right = six

    print(Solution().isValidBST(root))