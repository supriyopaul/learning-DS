'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_location = self.get_last_non_zero_location(nums)
        first_zero_location =  self.get_first_zero_location(nums, last_non_zero_location)
        self.lshift(nums, first_zero_location+1, last_non_zero_location)
        nums[last_non_zero_location] = 0
        return nums


    def get_last_non_zero_location(self, nums):
        for i in range(len(nums)-1,0,-1):
            if nums[i] != 0: return i
        return None
    def get_first_zero_location(self, nums, last_non_zero_location):
        for i in range(0, last_non_zero_location):
            if nums[i] == 0: return i
        return None
    def lshift(self, arr, l, r):
        import pdb; pdb.set_trace()
        if not l < r: return arr
        for i in range(l-1, r):
            arr[l] = arr[l+1]
        return arr


obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))
print(obj.moveZeroes([0]))
