from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sorted_nums = sorted(nums)
        left_index = 0
        right_index = len(nums) - 1
        while left_index != right_index:
            _sum = sorted_nums[left_index] + sorted_nums[right_index]
            print(_sum)
            if _sum == target:
                
                return [nums.index(sorted_nums[left_index]), (len(nums) - nums[::-1].index(sorted_nums[right_index]) - 1)]
            elif _sum < target:
                left_index += 1
            else:
                right_index -=1
            



if __name__ == "__main__":   
    obj = Solution()
    print(obj.twoSum(nums = [2,7,11,15], target = 9))
    print(obj.twoSum(nums = [3,2,4], target = 6))
    print(obj.twoSum(nums = [3,3], target = 6))