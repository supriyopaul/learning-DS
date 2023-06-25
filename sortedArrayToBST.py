from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        print(nums)
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])
        #if len(nums)%2 != 0: mid_index = int(len(nums) / 2)
        #else: mid_index = int(len(nums) / 2) - 1
        mid_index = int(len(nums)/2)
        result = TreeNode(nums[mid_index])
        result.left = self.sortedArrayToBST(nums[:mid_index])
        result.right = self.sortedArrayToBST(nums[mid_index+1:])

if __name__ == '__main__':
    # [-10,-3,0,5,9]
    print(Solution().sortedArrayToBST([-10,-3,0,5,9])) # [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]
    print(Solution().sortedArrayToBST([1,3])) # [1,3,] or [1,null,3]