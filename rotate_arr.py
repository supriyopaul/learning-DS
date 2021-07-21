from collections import deque

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

    def rotate2(self, nums, k):
        size = len(nums)
        q = deque()
        for i in range(size-k, size):
            q.append(nums[i])
        for i in range(0, size-k):
            q.append(nums[i])
        for i in range(len(nums)):
            nums[i] = q.popleft()
        return nums

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], 3))
print(obj.rotate2([1,2,3,4,5,6,7], 3))
