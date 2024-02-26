from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = end // 2

        while start <= end:
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start+end) // 2
        return -1

if __name__ == '__main__':
    print(Solution().search(nums = [-1,0,3,5,9,12], target = 9)) # 4
    print(Solution().search(nums = [-1,0,3,5,9,12], target = 2)) # -1
    print(Solution().search(nums = [0, 1, 2, 4, 5, 6, 7], target = 0)) # 0
    print(Solution().search(nums = [0, 1, 2, 4, 5, 6, 7], target = 7)) # -1
    print(Solution().search(nums = [1], target = 0)) # -1
    print(Solution().search(nums = [1, 3, 5], target = 0)) # -1