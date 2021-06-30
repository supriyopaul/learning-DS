'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

def get_sum_index(arr, num):
    for n in arr:
        if (num - n) in arr: return arr.index(n), arr.index(num -n)

def get_sum_index2(nums, target):
    sorted_nums = sorted(nums)
    left_index, right_index = 0, len(nums)-1
    while not left_index == right_index:
        summation = sorted_nums[left_index] + sorted_nums[right_index]
        if summation == target:
            return nums.index(sorted_nums[left_index]), nums.index(sorted_nums[right_index])
        elif summation > target:
            right_index = right_index - 1
        elif summation < target:
            left_index = left_index + 1
        else:
            return None, None

print(get_sum_index([3,2,4], 6))
print(get_sum_index2([3,2,4], 6))
