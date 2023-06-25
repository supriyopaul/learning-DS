from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combination_set = list(combinations(nums, 3))
        unique_zero_sum_combinations = set()
        result = []
        for combination in combination_set:
            c  = tuple(sorted(combination))
            if sum(c) == 0: unique_zero_sum_combinations.add(c)
        
        for combination in unique_zero_sum_combinations:
            result.append(list(combination))
        return result


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4])) # [[-1, 0, 1], [-1, 2, -1]]
    print(Solution().threeSum([0,1,1])) # []
    print(Solution().threeSum([0,0,0])) # [0,0,0]