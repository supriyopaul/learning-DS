from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            _sum = nums[left_index] + nums[right_index]
            if _sum == target:
                return [left_index+1, right_index+1]
            elif _sum < target:
                left_index += 1
            else:
                right_index -=1
            



if __name__ == "__main__":   
    obj = Solution()
    print(obj.twoSum(nums = [2,7,11,15], target = 9)) # [1, 2]
    print(obj.twoSum(nums = [2,3,4], target = 6)) # [2, 3]
    print(obj.twoSum(nums = [-1,0], target = -1)) # [1, 2]
    print(obj.twoSum(nums = [3,3], target = 6)) # [1, 2]