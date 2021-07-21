class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_size = len(nums)
        left = 0
        right = num_size -1
        while left <= right:
            print(left, right, nums)
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right = right - 1
                left = left + 1
            elif nums[left] == 0 and nums[right] == 0: right = right - 1
            elif nums[left] != 0 and nums[right] == 0: left = left + 1
            else: right = right - 1; left = left + 1
        return nums

print(Solution().moveZeroes([0,1,0,4,0,5,7,3,12]))
