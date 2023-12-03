from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            if target not in nums: return -1
            else: return nums.index(target)
        end = 0
        start = 1
        while nums[end] < nums[start] and start <= len(nums)-1:
            if start != len(nums)-1:
                end = start
                start += 1
            else:
                start = 0
                end = len(nums)-1
            
        
        if target >= nums[0] and target <= nums[end]:
            left, right = 0, end
        else:
            left, right = start, len(nums)-1

        while left <= right:
            mid = left + (right-left) //2

            if target == nums[mid]: return mid
            elif target < nums[mid]: right = mid
            else: left = mid+1
            if left == right == mid and not target == nums[mid]: return -1
        return -1

if __name__ == '__main__':
    print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0)) # 4 4->0 3->
    print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3)) # -1
    print(Solution().search(nums = [1], target = 0)) # -1
    print(Solution().search(nums = [1, 3, 5], target = 0)) # -1