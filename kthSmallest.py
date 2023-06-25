from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.counter = 0
        self.k = 0
        self.nodes_at_k = []

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            self.counter += 1
            if self.counter == self.k: self.nodes_at_k.append(root.val)
            self.inorder_traversal(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.inorder_traversal(root)
        return min(self.nodes_at_k)

if __name__ == "__main__":
    '''
    Input: root = [3,1,4,null,2], k = 1
    Output: 1
    '''
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthSmallest(root, k=1))

    '''
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3
    '''
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(Solution().kthSmallest(root, k=3))