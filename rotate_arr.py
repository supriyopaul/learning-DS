class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        new_nums = list()
        new_nums.extend(nums[size-k:size])
        new_nums.extend(nums[0:size-k])
        nums = new_nums
        return nums

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], 3))
