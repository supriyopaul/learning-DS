'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution(object):
    def maxSubArray(self, nums):
        left_element_index = 0
        right_element_index = len(nums)-1
        left_element = nums[left_element_index]
        right_element = nums[right_element_index]
        sum_dict = dict()
        if left_element_index == right_element_index: return sum(nums)
        while left_element_index != right_element_index:
            sum_dict[(left_element_index, right_element_index)] \
            = sum(nums[left_element_index:right_element_index+1])

            if left_element >= right_element:
                left_element_index += 1
                left_element = nums[left_element_index]
            else:
                right_element_index -= 1
                right_element = nums[right_element_index]
        print(sum_dict)
        return(max([sum_dict[k] for k in sum_dict]))

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.maxSubArray([1]))
print(obj.maxSubArray([5,4,-1,7,8]))
