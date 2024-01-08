from typing import List
from functools import reduce
from operator import mul

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        max_product = max(nums)
        for num in nums:
            if num == 0:
                cur_min, cur_max = 1, 1
            
            new_cur_min = min(num, num*cur_min, num*cur_max)
            cur_max = max(num, num*cur_min, num*cur_max)
            cur_min = new_cur_min
            max_product = max(max_product, cur_max)
            print(f'current_min: {cur_min}, current_max: {cur_max}')
        return max_product

            


if __name__ == "__main__":
    print(Solution().maxProduct(nums = [2,3,-2,4])) # 6
    print(Solution().maxProduct(nums = [-2,0,-1])) # 0
    print(Solution().maxProduct(nums = [-3,0,1,-2])) # 1
    print(Solution().maxProduct(nums = [-4,-3])) # -3