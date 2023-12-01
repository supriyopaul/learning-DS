from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        

        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        elif len(nums) == 3 and sum(nums) != 0 :
            return []
        
        result = set()
        
        for curr_index in range(len(nums)-2):
            left, right = curr_index+1, len(nums)-1
            sum_required = 0 - nums[curr_index]
            #print(sum_required)
            while left<right and nums[left] <= 0:
                triplet = tuple(sorted([nums[curr_index], nums[left], nums[right]]))
                #print(triplet)
                if nums[left] + nums[right] == sum_required:
                    result.add(triplet)
                    left += 1
                elif nums[left] + nums[right] < sum_required:
                    left += 1
                if nums[left] + nums[right] > sum_required:
                    right -= 1
            
        return [list(triples) for triples in result]


if __name__ == '__main__':
    print(Solution().threeSum([-4, -1, -1, 0, 1, 2])) # [[-1, 0, 1], [-1, 2, -1]]
    print(Solution().threeSum([0,1,1])) # []
    print(Solution().threeSum([0,0,0])) # [[0,0,0]]